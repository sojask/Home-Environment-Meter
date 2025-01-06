import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python Task_4.py <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    if response.status_code == 200:
        print(f"The website at {url} is working (HTTP {response.status_code}).")
    else:
        print(f"The website at {url} returned HTTP {response.status_code}.")
except requests.exceptions.RequestException as e:
    print(f"Error: Could not reach the website at {url}. Details: {e}")
