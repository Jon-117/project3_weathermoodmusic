"""
Grab location from API based on users input. Currently set up to search for city names based on input only in the United States.

Currently when looking up by state only returns the state instead of all cities in the state
"""

import requests
from classes import Location
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut



params = {
    'city': '',
    'country': 'United States',
    'format': 'json'
}


def get_location(user_input):
    """Gather all methods into one in order to create location object. 
    Only needs to call this function to excecute all of them."""
    try:
        create_params(user_input)
        returned_data = request_nominatim()
        result = format_data(returned_data)
        i = 0
        if len(result) > 1:
            for item in result:
                print(i,item.city_name,item.full_name)
                i+=1
            choice = int(input(f'Enter choice 0-{i-1}: '))
            return result[choice]
        return result[0]

    except requests.exceptions.HTTPError as e:
        print("An HTTP error has occurred.", e)
    except requests.exceptions.RequestException as e:
        print("An error has occurred.", e)



def create_params(user_input):
    """ Creates the search string for the api to search"""
    if user_input.isdigit():  # Prevents number input
        raise ValueError("Input must be a city name.")
    
    user_input = user_input
    search_string = f'{user_input}'
    params.update({'city': search_string})
    pass


def request_nominatim():
    response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
    data = response.json()
    return data


# def format_data(data):
#     locationsobjects = []
#     """ Formats the data by taking 'display_name' and splitting it into [city, county, state, country]
#     while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
#     for info in data:
#         location = info['display_name'].split(',')  # location is used in the UI to display the location to the user.
#         if len(location) > 4:  # Zip Code can appear between State and Country which this filters out.
#             location.remove(location[3])
#         # location.remove(location[3])
#         # location.remove(location[1])
#         city = location[0]
#         state = location[1]
#         # Latitude and longitude can be used for openweather to locate the area.
#         latitude = info['lat']
#         longitude = info['lon']
#         location_object = Location(city, state, latitude, longitude)
#         locationsobjects.append(location_object)
#     return locationsobjects

def format_data(data):
    locationsobjects = []
    """ Formats the data by taking 'display_name' and splitting it into [city, state, country]
    while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
    for info in data:
        location = info['display_name'].split(',')  # location is used in the UI to display the location to the user.
        # Extract city and state information
        city = location[0].strip()  # Remove leading/trailing whitespace
        state = location[-2].strip()  # Use the second to last element for the state
        # Latitude and longitude can be used for openweather to locate the area.
        latitude = info['lat']
        longitude = info['lon']
        location_object = Location(city, state, latitude, longitude)
        locationsobjects.append(location_object)
    return locationsobjects

    
def handleLocationSettings():
    pass
