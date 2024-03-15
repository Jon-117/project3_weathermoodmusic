import requests
import json
from pprint import pprint
import os

API_KEY = os.environ.get('OPENWEATHER_API_KEY')
url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    # 'q': 'minneapolis',
    'lat': 44.9,
    'lon': 93.2,
    'appid': API_KEY,
    'units': 'imperial'}

response = requests.get(url, params=params)
data = response.json()

pprint(data)

"""
example response data

{'base': 'stations',
 'clouds': {'all': 20},
 'cod': 200,
 'coord': {'lat': 44.98, 'lon': -93.2638},
 'dt': 1708306701,
 'id': 5037649,
 'main': {'feels_like': 19.44,
          'humidity': 72,
          'pressure': 1015,
          'temp': 28.18,
          'temp_max': 30.87,
          'temp_min': 24.39},
 'name': 'Minneapolis',
 'sys': {'country': 'US',
         'id': 2012563,
         'sunrise': 1708261812,
         'sunset': 1708299847,
         'type': 2},
 'timezone': -21600,
 'visibility': 10000,
 'weather': [{'description': 'few clouds',
              'icon': '02n',
              'id': 801,
              'main': 'Clouds'}],
 'wind': {'deg': 230, 'speed': 9.22}}


"""