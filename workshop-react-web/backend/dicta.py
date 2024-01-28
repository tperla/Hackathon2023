import requests
import json

# Define the API endpoint URL
url = "https://nakdan-string.loadbalancer.dicta.org.il/api"
def dictate(text:str):
    # Construct the request body
    data = {
        "data": text,
        "genre": "modern",
        "apiKey": "333b40e0-cd3a-4f22-9a9c-939c7bba21db"
    }

    # Send the POST request
    response = requests.post(url, json=data)

    # Process the response
    if response.ok:
        result = response.json()
        if result.get("error"):
            error_msg = result.get("msg")
            print(f"Error: {error_msg}")
        else:
            processed_string = result.get("data")
            return processed_string
    else:
        print(f"Request failed with status code {response.status_code}")
    
