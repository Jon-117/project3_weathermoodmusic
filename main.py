"""
Weathermood: A vehicle for nostalgia
"""

import ui
from classes import Weather, WeatherMood, build_weathermood_object, Location, Playlist
from get_location import get_location
from getWeatherForecast import get_weather_forecast
from spotify_api import search_spotify_playlists
from consolemenu import *
from consolemenu.items import *
from geopy.geocoders import Nominatim
import geopy.geocoders
import requests

one = WeatherMood(None, 0, 1710555589, 'Moscow', 'Idaho', 46.7323875, -117.000165, 47.25, 4.61, '01n', 'Clear',
                      53, 'Russian Cream',
                      'https://mosaic.scdn.co/640/ab67616d0000b27314d91ebdd6d7e2931322cc1aab67616d0000b2734db62465d930f949ecd18c38ab67616d0000b273565821887210741234f504e4ab67616d0000b273f2a7ea53a152b5b3ac9549a8',
                      'https://open.spotify.com/playlist/6s9bX6r6v6tPvpkB269GYo')
two = WeatherMood(None, 1, 1710557186.747964, 'Park Rapids', ' Minnesota', 46.9221813, -95.0586322, 48.13,
                      17.27, '04n', 'Clouds', 50, 'Clouds Radio',
                      'https://seeded-session-images.scdn.co/v2/img/122/secondary/track/03v70ZBxmcPX3RWAZMzqaW/en',
                      'https://open.spotify.com/playlist/37i9dQZF1E8QyZpgdVgaHA')
three = WeatherMood(None, 0, 1710557300.794149, 'Holly', ' Michigan', 42.7919727, -83.6277255, 37.09, 5.68,
                        '01n', 'Clear', 310, 'Timeless Nostalgic Hits',
                        'https://image-cdn-ak.spotifycdn.com/image/ab67706c0000bebb40557fc596eb62a51bfedd05',
                        'https://open.spotify.com/playlist/5wcoLsZw0Rp1rsB3ydxeJE')


fake_db = [one, two, three]
# validity checks








def is_valid_us_city(city_name):
    """Checks if a city name is a valid US city using multiple methods."""

    # Method 1: Using a pre-built dataset (if available)
    # with open("us_cities.txt", "r") as f:  # Replace with your city dataset
    #     us_cities = set(f.read().splitlines())
    # if city_name.lower() in us_cities:
    #     return True

    # Method 2: Using a geocoding service
    geolocator = geopy.geocoders.Nominatim(user_agent="city_validation_script")
    location = geolocator.geocode(city_name, country_codes="US")
    if location and location.address.split(",")[-1].strip() == "United States":
        return True
    return False



moods = [
  "happy", "sad", "angry", "excited", "calm",
  "frustrated", "joyful", "peaceful", "hopeful",
  "melancholy", "content", "proud", "grateful",
  "stressed", "anxious", "loving", "caring",
  "bored", "curious", "energetic", "sleepy"
]
def create_new_weathermood():  # Functionally works, just need DB connection to store new WM objects.
    """
    Create a new weathermood. Main function for creating a new weathermood, tying all api together.
    """
    isrun = True
    while isrun:
        user_city = ui.get_user_input("What city are you in?  ")
        if user_city.isdigit():
            print('\nInput must be a valid city\n')
            continue
        if is_valid_us_city(user_city) == False:
            print("\nInput must be a valid city\n")
            continue
        user_mood = ui.get_user_input("What's your mood?  ")
        if user_mood.isdigit():  # Prevents number input
            print("\nInput must be a valid mood\n")
            continue
        if user_mood.lower() not in moods:
            print("\nInput must be a valid mood\n")
            continue
        isrun = False
    location = get_location(user_city)
    # Todo - add location verification - currently bad response does not ask for readjustment
    weather = get_weather_forecast(location.latitude, location.longitude)
    spotify_query = f'{user_mood} {weather.conditions} {location.city_name}'

    playlist = search_spotify_playlists(spotify_query)
    # print(isinstance(playlist, Playlist))

    weather_mood = build_weathermood_object(location, weather, playlist)
    weather_mood.open_link()
    # TODO - Store the object in database
    print(weather_mood.display_string())
    fake_db.append(weather_mood)
    print(weather_mood.weather_mood_object_string())
    return weather_mood


def toggle_favorite(wm):
    wm.favorite = 1 if wm.favorite == 0 else 0
    # Update the database


def generate_wm_menu(wm, parent_menu):
    wm_menu = ConsoleMenu(f"{wm.display_string()}", exit_option_text='Go Back')
    wm_menu.append_item(FunctionItem("Open Link", wm.open_link))
    wm_menu.append_item(FunctionItem("Toggle Favorite/Unfavorite", toggle_favorite, args=[wm]))
    return SubmenuItem(f"{wm.display_string()}", wm_menu, parent_menu)


def generate_weathermoods_submenu(weathermoods, title, parent_menu):
    submenu = ConsoleMenu(title, exit_option_text=f'Return to {parent_menu.title}')
    for wm in weathermoods:
        wm_submenu_item = generate_wm_menu(wm, submenu)
        submenu.append_item(wm_submenu_item)
    return SubmenuItem(title, submenu, parent_menu)


def main_menu():
    try:
        menu = ConsoleMenu("Main Menu", exit_option_text='Exit')

        # Create New WeatherMood item
        menu.append_item(FunctionItem("Create new", create_new_weathermood))

        # Submenu for Past WeatherMoods
        past_weathermoods_menu = ConsoleMenu("Past WeatherMoods", exit_option_text='Return to Main Menu')

        # Favorites submenu
        favorite_weathermoods = [wm for wm in get_weathermoods_from_db() if wm.favorite]
        favorites_submenu = generate_weathermoods_submenu(favorite_weathermoods, "Favorites", past_weathermoods_menu)
        past_weathermoods_menu.append_item(favorites_submenu)

        # All objects submenu
        all_weathermoods = get_weathermoods_from_db()
        all_submenu = generate_weathermoods_submenu(all_weathermoods, "All", past_weathermoods_menu)
        past_weathermoods_menu.append_item(all_submenu)

        menu.append_item(SubmenuItem("Previously Created", past_weathermoods_menu, menu))

        menu.show()
    except:
        menu.show()


def get_weathermoods_from_db():
    # Placeholder: Fetch weathermood objects from the database
    # return a list of weathermoods

    one = WeatherMood(None, 0, 1710555589, 'Moscow', 'Idaho', 46.7323875, -117.000165, 47.25, 4.61, '01n', 'Clear',
                      53, 'Russian Cream',
                      'https://mosaic.scdn.co/640/ab67616d0000b27314d91ebdd6d7e2931322cc1aab67616d0000b2734db62465d930f949ecd18c38ab67616d0000b273565821887210741234f504e4ab67616d0000b273f2a7ea53a152b5b3ac9549a8',
                      'https://open.spotify.com/playlist/6s9bX6r6v6tPvpkB269GYo')
    two = WeatherMood(None, 1, 1710557186.747964, 'Park Rapids', ' Minnesota', 46.9221813, -95.0586322, 48.13,
                      17.27, '04n', 'Clouds', 50, 'Clouds Radio',
                      'https://seeded-session-images.scdn.co/v2/img/122/secondary/track/03v70ZBxmcPX3RWAZMzqaW/en',
                      'https://open.spotify.com/playlist/37i9dQZF1E8QyZpgdVgaHA')
    three = WeatherMood(None, 0, 1710557300.794149, 'Holly', ' Michigan', 42.7919727, -83.6277255, 37.09, 5.68,
                        '01n', 'Clear', 310, 'Timeless Nostalgic Hits',
                        'https://image-cdn-ak.spotifycdn.com/image/ab67706c0000bebb40557fc596eb62a51bfedd05',
                        'https://open.spotify.com/playlist/5wcoLsZw0Rp1rsB3ydxeJE')

    return [one, two, three]


if __name__ == "__main__":
    main_menu()
