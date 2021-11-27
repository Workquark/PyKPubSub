import time
from restaurants.restaurant import Restaurant
from producer import getRestaurants
from timeloop import Timeloop
from datetime import timedelta
from munch import Munch

tl = Timeloop()

@tl.job(interval=timedelta(seconds=2))
def train_model():
    my_restaurants:list[Restaurant] = []
    response = getRestaurants()
    for item in response.json(): my_restaurants.append(Munch(item))
    lambda_cube = lambda y: print(y.name)
    for res in my_restaurants: lambda_cube(res)