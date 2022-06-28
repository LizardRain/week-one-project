import requests

url = "https://www.bugsnaxapi.com/api/bugsnax/"

response = requests.get(url)

res = response.json()
data = res['bugsnax']

for item in data:
	print(item)
