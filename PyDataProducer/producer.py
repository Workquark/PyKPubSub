import requests


def getRestaurants():
    response = requests.get("https://random-data-api.com/api/restaurant/random_restaurant?size=3")
    return response