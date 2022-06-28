import requests

url = "https://www.bugsnaxapi.com/api/"

response = requests.get(url)

print(response.json())
