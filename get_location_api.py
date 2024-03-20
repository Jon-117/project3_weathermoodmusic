"""
Grab location from API based on users input.

Currently set up to search for city names.
"""

import requests

import ui
from classes import Location
import logging

log = logging.getLogger(__name__)

params = {
    'city': '',
    'country': 'United States',
    'format': 'json'
}


def get_location(user_input) -> Location or None:
    """
    Create location object from user input.

    :param user_input:      `str`: A city's name
    :return:                `Location` or `None` if city not found.
    """

    create_params(user_input)
    returned_data = request_nominatim()
    check_if_input_city = confirm_data(returned_data)
    if check_if_input_city:
            result = format_data(check_if_input_city) 
    else:
        raise ValueError('AddressType Error: User input is not a city.')
    if returned_data is None:
        log.error(f'City not found. Is "{user_input}" a valid city?')
        raise LocationError(f'City not found. Is "{user_input}" a valid city?')
    if len(result) > 1:
        return ui.get_selection(result)
    elif len(result) == 1:
        return result[0]


def create_params(user_input):
    """ Creates the search string for the api to search"""
    if user_input.isdigit():  # Prevents number input
        raise ValueError("Input must be a city name not numbers.")
    log.debug(f'Assigning params for {user_input}')
    params.update({'city': f'{user_input}'})
    pass


def request_nominatim():
    """
    Try searching nominatum for city name, return supplied data as json.
    """
    try:
        response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
        data = response.json()
        if len(data) == 0:
            raise LocationError(f'City not found.')
        return data

    except LocationError as e:
        log.error(f'{e}')
        ui.alert(f'Error getting location: {e}')
        return None

    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        ui.alert(f'HTTP error occurred: {http_err}')
        return None

    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f'Error connecting to the server: {conn_err}')
        ui.alert(f'Error connecting to the server: {conn_err}')
        return None

    except requests.exceptions.Timeout as timeout_err:
        logging.error(f'Timeout error occurred: {timeout_err}')
        ui.alert(f'Timeout error occurred: {timeout_err}')
        return None

    except requests.exceptions.RequestException as req_err:
        logging.error(f'An error occurred while making the request: {req_err}')
        ui.alert(f'An error occurred while making the request: {req_err}')
        return None

def confirm_data(data):
    cities = []
    acceptable_address_type = ['town', 'city']
    for info in data:
        if info['addresstype'] in acceptable_address_type:
            cities.append(info)
        else:
            data.remove(info)
    if len(cities) == 0:
        return False
    else:
        return cities

def format_data(data):
    """ Formats the data by taking 'display_name' and splitting it into [city, county, state, country]
    while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
    log.info(f'Creating location objects from supplied json data... ')
    log.debug(f'{len(data)} locations in data supplied to `format_data()`')
    try:
        if len(data) == 0:
            raise LocationError(f'No locations available in response data')
        location_objects = []
        for city in data:
            full_name_split = city["display_name"].split(',')  # location is used in the UI to display the location to the user.      
            if len(full_name_split) > 4:  # Zip Code can appear between State and Country which this filters out.
                full_name_split.remove(full_name_split[3])
            city_name = city['name']
            full_name = ', '.join(full_name_split)
            # Latitude and longitude can be used for openweather to locate the area.
            latitude = city['lat']
            longitude = city['lon']
            location_object = Location(city_name, full_name, latitude, longitude)
            location_objects.append(location_object)
        log.debug(f'Formatted json data successfully. {len(location_objects)} location objects created.')
        return location_objects
    except LocationError as e:
        log.error(f'Error getting location: {e}')
        ui.alert(f'Error getting location: {e}')

class LocationError(Exception):
    def __init__(self, message='Error while creating location. Please try again.'):
        self.message = message
        super().__init__(
            message)  # Remember, super() calls the parent's __init__ to inherit initialization properties. Also allows our custom exception to be caught by `except`

