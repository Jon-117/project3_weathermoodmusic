import requests
from pprint import pprint
import unittest


params = {
    'q': 'minneapolis',
    'format': 'json'
}
response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
data = response.json()

def test_minneapolis():
    for result in data:
        name = result['display_name']
        print(name)

test()


"""
example response data

[{'addresstype': 'city',
  'boundingbox': ['44.8901500', '45.0512500', '-93.3291271', '-93.1938590'],
  'class': 'boundary',
  'display_name': 'Minneapolis, Hennepin County, Minnesota, United States',
  'importance': 0.6371693135985456,
  'lat': '44.9772995',
  'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. '
             'http://osm.org/copyright',
  'lon': '-93.2654692',
  'name': 'Minneapolis',
  'osm_id': 136712,
  'osm_type': 'relation',
  'place_id': 29019823,
  'place_rank': 16,
  'type': 'administrative'},
 {'addresstype': 'town',
  'boundingbox': ['39.1140825', '39.1322656', '-97.7246031', '-97.6878841'],
  'class': 'boundary',
  'display_name': 'Minneapolis, Ottawa County, Kansas, United States',
  'importance': 0.4283953917728152,
  'lat': '39.1223968',
  'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. '
             'http://osm.org/copyright',
  'lon': '-97.7087076',
  'name': 'Minneapolis',
  'osm_id': 130006,
  'osm_type': 'relation',
  'place_id': 316616611,
  'place_rank': 16,
  'type': 'administrative'}]


"""
