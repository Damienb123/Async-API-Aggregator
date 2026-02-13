# API imports for concurrent calls
import asyncio
import aiohttp
import json

# Asynchronously fetches data from the url
async def fetch_async(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return url, await response.json()
        else:
            print(f"Error fetching {url}: Status code {response.status}")
            return url, None
# main for declaring api endpoints for comparison        
async def main():
    api_endpoints = {
        "https://official-joke-api.appspot.com/random_joke",
        "https://api.agify.io?name=meelad",
        "https://api.nationalize.io?name=nathaniel"
    }
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in api_endpoints]
        results_list = await asyncio.gather(*tasks)

        results = dict(results_list)
        print()
        print(json.dumps(results, indent=4))
        print()

if __name__ == "__main__":
    asyncio.run(main())


