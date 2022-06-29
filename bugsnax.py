import requests

url = "https://www.bugsnaxapi.com/api"


def get_bugsnax():
    response = requests.get(url + '/bugsnax')
    res =  response.json()
    return res['bugsnax']


def get_location():
    response = requests.get(url + '/locations')
    return response.json()


def get_grumpus():
    response = requests.get(url + '/grumpuses')
    return response.json()
