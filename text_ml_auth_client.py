import requests
import json

url = "http://127.0.0.1:8000/"
import sys

# Load API key from file
try:
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    print("api_key.txt not found. Please create this file with your API key.")
    sys.exit(1)

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}
data = {
    "text": "Ray is a framework for building scalable applications. It is the most powerful distributed computing framework for Python."
    # "text": "My name is Jalaj. I'm a software engineer. I love coding."
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)

# Prepare request manually to print it before sending
# session = requests.Session()
# request = requests.Request("POST", url, headers=headers, json=data)
# prepared = session.prepare_request(request)

# # Print full request
# print("=== REQUEST ===")
# print(f"{prepared.method} {prepared.url}")
# print("Headers:")
# print(json.dumps(dict(prepared.headers), indent=2))
# print("Body:")
# print(prepared.body.decode() if isinstance(prepared.body, bytes) else prepared.body)

# # Send request
# response = session.send(prepared)

# # Print full response
# print("\n=== RESPONSE ===")
# print(f"Status Code: {response.status_code}")
# print("Headers:")
# print(json.dumps(dict(response.headers), indent=2))
# print("Body:")
# print(response.text)

