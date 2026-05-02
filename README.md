# Async-API-Aggregator
A high-performance, asynchronous API aggregation service built with Python and FastAPI. This project demonstrates how to efficiently fetch and unify data from multiple external APIs concurrently while maintaining clean structure, error handling, and extensibility.

## Overview
This service queries multiple third-party APIs in parallel and returns a standardized, structured response. It is designed to:

- Reduce total latency using asynchronous I/O
- Provide consistent response formatting across different APIs
- Gracefully handle failures without breaking the entire request
- Serve as a scalable foundation for microservice aggregation patterns

## Tech Stack
- FastAPI – API framework
- aiohttp – Async HTTP client
- asyncio – Concurrency management
- Pydantic – Data validation and schema modeling

## Key Features
### Concurrent API Requests
All external API calls are executed in parallel using `asyncio.gather()`, ensuring fast response times.
### Strutured Response Model
Each API response is normalized into a consistent schema:
```
{
  "success": true,
  "data": {...},
  "error": null,
  "status_code": 200
}
```
### Fault Tolerance
Failures in inidividual APIs `not` break the entire aggregation. Each API response is isolated and handled independently.
### Extensible Design
API endpoints are defined as structured objects, making it easy to:
- Add new APIs
- Introduce authentication
- Configure per-endpoint settings

## API's Used
- Official Joke API – returns a random joke
- Agify API – predicts age based on a name
- Nationalize API – predicts nationality probabilities based on a name

***All API's are public and require no authentication***

## Requirements
- Python 3.9+
- aiohttp

## Example Output

```
{
  "joke": {
    "success": true,
    "data": {
      "setup": "Why did the scarecrow win an award?",
      "punchline": "Because he was outstanding in his field!"
    },
    "error": null,
    "status_code": 200
  },
  "agify": {
    "success": true,
    "data": {
      "name": "meelad",
      "age": 32
    },
    "error": null,
    "status_code": 200
  },
  "nationalize": {
    "success": true,
    "data": {
      "name": "nathaniel",
      "country": []
    },
    "error": null,
    "status_code": 200
  }
}
```

## How it Works
1. API endpoints are defined using the `APIEndpoint` model
2. A shared async HTTP session is created with a timeout
3. Each API is called concurrently using `fetch_async()`
4. Results are gathered and converted into a dicionary
5. The final response is returned using a typed schema


### API URLs
```
[["https://official-joke-api.appspot.com/random_joke",{"type":"general","setup":"I'm reading a book about anti-gravity...","punchline":"It's impossible to put down","id":37}],["https://api.agify.io?name=meelad",{"count":21,"name":"meelad","age":36}],["https://api.nationalize.io?name=nathaniel",{"count":6172,"name":"nathaniel","country":[{"country_id":"NG","probability":0.17632453512718907},{"country_id":"GH","probability":0.08304361297013127},{"country_id":"NE","probability":0.07164615880444838},{"country_id":"US","probability":0.032019319698424385},{"country_id":"ID","probability":0.02637540425400123}]}]]
```
