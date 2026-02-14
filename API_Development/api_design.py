# API imports for concurrent calls and FastAPI service
import asyncio
import aiohttp
from fastapi import FastAPI
# Initialize FastAPI app
app = FastAPI(title="Async API Aggregator")

# Helper function to fetch data from a single API endpoint asynchronously
async def fetch_async(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return url, await response.json()
            return url, {"error": f"Failed to fetch data, status code: {response.status}"}
    except Exception as e:
        return url, {"error": str(e)} 
# Endpoint to aggregate data from multiple APIs concurrently
@app.get("/aggregate")      
async def aggregate():
    # change for readability
    api_endpoints = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://api.agify.io?name=meelad",
        "https://api.nationalize.io?name=nathaniel"
    ]
    # Use aiohttp to make concurrent API calls
    timeout = aiohttp.ClientTimeout(total=5)  # Set a timeout for the requests
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch_async(session, url) for url in api_endpoints]
        results = await asyncio.gather(*tasks)

        return results
    

