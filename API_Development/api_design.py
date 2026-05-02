import asyncio
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel, Field


class APIEndpoint(BaseModel):
    # Keeping endpoint metadata structured makes it easier to add labels,
    # auth settings, or per-API options later without changing fetch logic.
    name: str
    url: str


class APIResponse(BaseModel):
    # Every upstream API returns different JSON, so the wrapper standardizes
    # successes, error, and status details while leaving the original payload intact.
    success: bool
    data: dict | list | None = None
    error: str | None = None
    status_code: int | None = Field(default=None, ge=100, le=599)


AggregateResponse = dict[str, APIResponse]


app = FastAPI(title="Async API Aggregator")


API_ENDPOINTS = [
    # Names become stable response keys for clients, avoiding brittle URL-based output.
    APIEndpoint(
        name="joke",
        url="https://official-joke-api.appspot.com/random_joke",
    ),
    APIEndpoint(
        name="agify",
        url="https://api.agify.io?name=meelad",
    ),
    APIEndpoint(
        name="nationalize",
        url="https://api.nationalize.io?name=nathaniel",
    ),
]


async def fetch_async(
    session: aiohttp.ClientSession,
    endpoint: APIEndpoint,
) -> tuple[str, APIResponse]:
    try:
        async with session.get(endpoint.url) as response:
            # Return the endpoint name with its typed response so gather()
            # can be converted directly into the final dictionary.
            if response.status == 200:
                return endpoint.name, APIResponse(
                    success=True,
                    data=await response.json(),
                    status_code=response.status,
                )

            return endpoint.name, APIResponse(
                success=False,
                error="Failed to fetch data",
                status_code=response.status,
            )
    except Exception as e:
        # A single API failure should not fail the whole aggregation request.
        return endpoint.name, APIResponse(success=False, error=str(e))

@app.get("/aggregate", response_model=AggregateResponse)
async def aggregate() -> AggregateResponse:
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # Concurrent fetches keep total latency close to the slowest API call
        # instead of the sume of all API response times.
        tasks = [fetch_async(session, endpoint) for endpoint in API_ENDPOINTS]
        results = await asyncio.gather(*tasks)
        return dict(results)
