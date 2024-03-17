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


def get_location(user_input):
    """
    Create location object from user input.
    :param user_input:      str: A city's name
    """
    try:
        create_params(user_input)
        returned_data = request_nominatim()
        result = format_data(returned_data)
        i = 0
        if len(result) > 1:
            for item in result:
                print(i, item.city_name, item.full_name)
                i += 1
            choice = int(ui.get_user_input(f'Enter choice 0-{i - 1}: ', True))
            return result[choice]
        return result[0]

    except requests.exceptions.HTTPError as e:
        print("An HTTP error has occurred.", e)
    except requests.exceptions.RequestException as e:
        print("An error has occurred.", e)


def create_params(user_input):
    """ Creates the search string for the api to search"""
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
        return data


    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        ui.alert(f'HTTP error occurred: {http_err}')

    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f'Error connecting to the server: {conn_err}')
        ui.alert(f'Error connecting to the server: {conn_err}')

    except requests.exceptions.Timeout as timeout_err:
        logging.error(f'Timeout error occurred: {timeout_err}')
        ui.alert(f'Timeout error occurred: {timeout_err}')

    except requests.exceptions.RequestException as req_err:
        logging.error(f'An error occurred while making the request: {req_err}')
        ui.alert(f'An error occurred while making the request: {req_err}')

    return None


def format_data(data):
    """ Formats the data by taking 'display_name' and splitting it into [city, county, state, country]
    while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
    log.info(f'Creating location objects from supplied json data... ')
    location_objects = []
    for info in data:
        location = info['display_name'].split(',')  # location is used in the UI to display the location to the user.
        if len(location) > 4:  # Zip Code can appear between State and Country which this filters out.
            location.remove(location[3])
        # location.remove(location[3])
        # location.remove(location[1])
        city = location[0]
        state = location[1]
        # Latitude and longitude can be used for openweather to locate the area.
        latitude = info['lat']
        longitude = info['lon']
        location_object = Location(city, state, latitude, longitude)
        location_objects.append(location_object)
    log.debug(f'Formatted json data successfully. {len(location_objects)} location objects created.')
    return location_objects
