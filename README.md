# Async-API-Aggregator
A light weight Python project that demonstrates concurrent API requests using asyncio and aiohttp.
The script fetches data from multiple public API's simultaneously and prints the aggregated JSON response in a readable format.

## Features
- Asynchronous HTTP requests with aiohttp
- Concurrent API calls using asyncio.gather
- Clean JSON output formatting
- Simple, extensible structure for adding more API's

## Purpose
This project was built to practice and demonstrate:
- Asynchronous programming in Python
- Making concurrent external API calls
- Handling JSON responses
- Aggregating results into a single output

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
    "https://official-joke-api.appspot.com/random_joke": {
        "type": "programming",
        "setup": "Why did the programmer always carry a pencil?",
        "punchline": "They preferred to write in C#.",
        "id": 448
    },
    "https://api.nationalize.io?name=nathaniel": {
        "count": 6172,
        "name": "nathaniel",
        "country": [
            {
                "country_id": "NG",
                "probability": 0.17632453512718907
            },
            {
                "country_id": "GH",
                "probability": 0.08304361297013127
            },
            {
                "country_id": "NE",
                "probability": 0.07164615880444838
            },
            {
                "country_id": "US",
                "probability": 0.032019319698424385
            },
            {
                "country_id": "ID",
                "probability": 0.02637540425400123
            }
        ]
    },
    "https://api.agify.io?name=meelad": {
        "count": 21,
        "name": "meelad",
        "age": 36
    }
}
```

## Codebase Enhancement
In recent changes to the codebase, a backend API service was integrated using FastAPI while still applying asynchronous fetches of data within the URLs. aiohttp is still used to make concurrent API calls as well. Try and Except error handling is utilized to ensure success and/or failures while fetching data.

Reference PR https://github.com/Damienb123/Async-API-Aggregator/pull/3 for recent changes to the codebase.
## Example Output
### JSON Formatted
```
[
    [
        "https://official-joke-api.appspot.com/random_joke",
        {
            "type": "general",
            "setup": "I'm reading a book about anti-gravity...",
            "punchline": "It's impossible to put down",
            "id": 37
        }
    ],
    [
        "https://api.agify.io?name=meelad",
        {
            "count": 21,
            "name": "meelad",
            "age": 36
        }
    ],
    [
        "https://api.nationalize.io?name=nathaniel",
        {
            "count": 6172,
            "name": "nathaniel",
            "country": [
                {
                    "country_id": "NG",
                    "probability": 0.17632453512718907
                },
                {
                    "country_id": "GH",
                    "probability": 0.08304361297013127
                },
                {
                    "country_id": "NE",
                    "probability": 0.07164615880444838
                },
                {
                    "country_id": "US",
                    "probability": 0.032019319698424385
                },
                {
                    "country_id": "ID",
                    "probability": 0.02637540425400123
                }
            ]
        }
    ]
]
```
### API URL
```
[["https://official-joke-api.appspot.com/random_joke",{"type":"general","setup":"I'm reading a book about anti-gravity...","punchline":"It's impossible to put down","id":37}],["https://api.agify.io?name=meelad",{"count":21,"name":"meelad","age":36}],["https://api.nationalize.io?name=nathaniel",{"count":6172,"name":"nathaniel","country":[{"country_id":"NG","probability":0.17632453512718907},{"country_id":"GH","probability":0.08304361297013127},{"country_id":"NE","probability":0.07164615880444838},{"country_id":"US","probability":0.032019319698424385},{"country_id":"ID","probability":0.02637540425400123}]}]]
```
