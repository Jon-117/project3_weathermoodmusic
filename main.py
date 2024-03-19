"""
Weathermood: A vehicle for nostalgia
"""

import ui
from classes import Weather, Location, Playlist, WeatherMood, WeatherMoodLibrary, build_weathermood_object, WeatherMoodErrors
from get_location_api import get_location
from getWeatherForecast import get_weather_forecast
from spotify_api import search_spotify_playlists
from consolemenu import *
from consolemenu.items import *
import time


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


def create_new_weathermood(selected_location, user_mood):  # Functionally works, just need DB connection to store new WM objects.
    """
    Create a new weathermood. Main function for creating a new weathermood, tying all api together.
    """
    library = WeatherMoodLibrary()
    location = selected_location
    city_name, full_name, latitude, longitude = location.city_name, location.full_name, location.latitude, location.longitude
    # Todo - add location verification - currently bad response does not ask for readjustment
    weather = get_weather_forecast(latitude, longitude)
    spotify_query = f"{user_mood} {weather.conditions} {city_name}"
    playlist = search_spotify_playlists(spotify_query)
    # print(isinstance(playlist, Playlist))

    weather_mood = build_weathermood_object(location, weather, playlist)
    # TODO - Store the object in database
    library.add_playlist(weather_mood) # This should add the 'built' weather mood to the database.
    ui.clear_screen()
    print(weather_mood.display_string())
    time.sleep(5)

def toggle_favorite(wm):
    wm.favorite = 1 if wm.favorite == 0 else 0
    # Update the database

def generate_wm_menu(wm, parent_menu):
    wm_menu = ConsoleMenu(f"{wm.display_string()}", exit_option_text='Go Back') # exit_option_text may not be necessary.
    wm_menu.append_item(FunctionItem("Open Link", wm.open_link))
    wm_menu.append_item(FunctionItem("Toggle Favorite/Unfavorite", toggle_favorite, args=[wm]))
    return SubmenuItem(f"{wm.display_string()}", wm_menu, parent_menu)

def generate_weathermoods_submenu(weathermoods, title, parent_menu):
    submenu = ConsoleMenu(title, exit_option_text=f'Return to {parent_menu.title}')
    for wm in weathermoods:
        wm_submenu_item = generate_wm_menu(wm, submenu)
        submenu.append_item(wm_submenu_item)

    return SubmenuItem(title, submenu, parent_menu)

def get_all_weatherMoods_from_db():
    # Placeholder: Fetch weathermood objects from the database
    # return a list of weathermoods
    library = WeatherMoodLibrary()
    returned_data = library.list_all_playlists()
    return returned_data

def get_favorite_weatherMoods_from_db():
    library = WeatherMoodLibrary()
    returned_favorites = library.display_favorites(True)
    return returned_favorites

def get_location_input():
    user_city = ui.get_user_input("What city are you in?  ")
    chosen_location = return_location_options(user_city)
    user_mood = ui.get_user_input("\nWhat's your mood? ")
    create_new_weathermood(chosen_location, user_mood) 
    
def return_location_options(user_city):
    location = get_location(user_city)
    while True:
        ui.clear_screen()
        choices = []
        for place in location:
            location_full_name = place['full_name']
            print(location_full_name)
            choices.append(location_full_name)
        selected_location = ui.get_user_input("\nSelect one of the options *Type the name out exactly*: ").title().strip()
        if selected_location in choices:
            for place in location:
                if selected_location in place['full_name']:
                        location = Location(place['city_name'], place['full_name'], place['latitude'], place['longitude'])
                        return location
        else:
            raise WeatherMoodErrors("That is not an option. Please enter it exactly as shown.")


def main_menu():
    menu = ConsoleMenu("Main Menu", exit_option_text='Exit')

    menu.append_item(FunctionItem("Select Location", get_location_input))

    # Submenu for Past WeatherMoods
    past_weathermoods_menu = ConsoleMenu("Recent WeatherMoods", exit_option_text='Return to Main Menu')

    # Favorites submenu
    favorite_weathermoods = get_favorite_weatherMoods_from_db() # List of locations
    favorites_submenu = generate_weathermoods_submenu(favorite_weathermoods, "Favorites", past_weathermoods_menu)
    past_weathermoods_menu.append_item(favorites_submenu)

    # All objects submenu
    all_weathermoods = get_all_weatherMoods_from_db() # content
    all_submenu = generate_weathermoods_submenu(all_weathermoods, "All", past_weathermoods_menu) # (content, title, menu name)
    past_weathermoods_menu.append_item(all_submenu)

    menu.append_item(SubmenuItem("Previously Created", past_weathermoods_menu, menu))

    menu.show()


if __name__ == "__main__":
    main_menu()
