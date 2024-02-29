"""Grab location from API based on users input. Currently set up to search for city names based on input only in the United States."""
""" Currently when looking up by state only returns the state instead of all cities in the state"""
import requests

params = {
    'city': '',
    'country': 'United States',
    'format': 'json'
}

def main():
    userInput = input('Enter a city: ') #Take out and connect with UI
    get_location(userInput)
    returned_data = request_nominatim()
    format_data(returned_data)


def get_location(userInput):
    """ Creates the search string for the api to search"""
    userInput = userInput
    searchString = f'{userInput}'
    params.update({'city': searchString})
    pass

def request_nominatim():
    response = requests.get('https://nominatim.openstreetmap.org/search', params = params)
    data = response.json()
    return data

def format_data(data):
    """ Formats the data by taking 'display_name' and splitting it into [city, county, state, country]
    while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
    places = []
    for info in data:
        lat_and_lon = [] # Latitude and longitude can be used for openweather to locate the area.
        location = info['display_name'].split(',') # location is used in the UI to display the location to the user.
        if len(location) > 4: # Zip Code can appear between State and Country which this filters out.
            location.remove(location[3])
        lat_and_lon.append(info['lat'])
        lat_and_lon.append(info['lon'])
        location.append(lat_and_lon)
        places.append(location)

    #return "location, lat_and_lon"
              
    
main()



"""
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
