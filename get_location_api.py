"""
Currently when looking up by state only returns the state instead of all cities in the state
"""
import requests
from classes import WeatherMoodErrors

params = {
    'city': '',
    'country': 'United States',
    'format': 'json',
}

def get_location(user_input):
    """Gather all methods into one in order to create location object. 
    Only needs to call this function to excecute all of them."""
    try:
        create_params(user_input)
        returned_data = request_nominatim()
        check_if_input_city = confirm_data(returned_data)
        if check_if_input_city:
            actual_cities = format_data(check_if_input_city) 
        else:
            raise WeatherMoodErrors('AddressType Error: User input is not a city.')
        return actual_cities # Display options to user
    except requests.exceptions.HTTPError as e:
        print("An HTTP error has occurred.", e)
    except requests.exceptions.RequestException as e:
        print("An error has occurred.", e)

def create_params(user_input):
    """ Creates the search string for the api to search"""
    if user_input.isdigit():  # Prevents number input
        raise ValueError("Input must be a city name not numbers.")
    search_string = f'{user_input}'
    params.update({'city': search_string})

def request_nominatim():
    response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
    data = response.json()
    return data

def confirm_data(data):
    cities = []
    acceptable_address_type = ['town', 'city']
    for info in data:
        location = info['display_name'].split(',')  # location is used in the UI to display the location to the user.
        #print(f"Before filter: {location} {info['addresstype']}")
        if info['addresstype'] in acceptable_address_type:
            cities.append(info)
        else:
            data.remove(info)
            print(f"DELETED: {location}, {info['lat']},{info['lon']}, {info['addresstype']}")
    if len(cities) == 0:
        return False
    else:
        return cities

def format_data(check_if_input_city):
    """ Formats the data by taking 'display_name' and splitting it into [city, county, state, country]
    while filtering out unnecessary info. The location names will be used for display purposes and long and lat will be used for openweather"""
    formatted_data = []
    for info in check_if_input_city:
        location = info['display_name'].split(',')  # location is used in the UI to display the location to the user.
        if len(location) > 4:  # Zip Code can appear between State and Country which this filters out.
            location.remove(location[3])
        if len(location) == 4:
            location.remove(location[3]) # Removes Country
            location.remove(location[1]) # Removes County

        city = location[0]
        full_name = f'{location[0]},{location[1]}'
        latitude = info['lat']
        longitude = info['lon']
        print(location)
        combine_attributes = {
            'city_name': city,
            'full_name': full_name,
            'latitude': latitude,
            'longitude': longitude
        }
        formatted_data.append(combine_attributes)
    return formatted_data

