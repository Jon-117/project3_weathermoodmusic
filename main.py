"""
Weathermood: A vehicle for nostalgia
"""

import ui
from classes import WeatherMood, build_weathermood_object
from get_location import get_location
from getWeatherForecast import get_weather_forecast
from spotify_api import search_spotify_playlists
from consolemenu import *
from consolemenu.items import *
import database_manager
from database_manager import DatabaseManager
import logging as log


# TODO - Figure out why the menu isn't refreshing data when making db changes.
#           (keeps data static from point of app start)

def create_new_weathermood():
    """
    Create a new weathermood. Main function for creating a new weathermood, tying all api together.
    """
    log.info('Creating a new weathermood...')

    # TODO - Add validation: No empty strings.
    user_city = ""
    while user_city == "":
        user_city = ui.get_user_input("What city are you in?  ")
    user_mood = ""
    while user_mood == "":
        user_mood = ui.get_user_input("What's your mood?  ")
    log.debug('User inputs received...')
    log.debug(f'Calling get_location({user_city})')
    location = get_location(user_city)
    log.info(f'Location object created: {location.city_name}: {location.latitude}, {location.longitude}')
    # Todo - add location verification - currently bad response does not ask for readjustment
    weather = get_weather_forecast(location.latitude, location.longitude)
    spotify_query = f'{user_mood} {weather.conditions} {location.city_name}'

    playlist = search_spotify_playlists(spotify_query)
    # print(isinstance(playlist, Playlist))

    weather_mood = build_weathermood_object(location, weather, playlist)
    weather_mood.open_link()
    DatabaseManager.add_weathermood(weather_mood)
    # print(weather_mood.display_string())
    # print(weather_mood.weather_mood_object_string())



def toggle_favorite(wm):
    DatabaseManager.toggle_favorite(wm)


def delete_weathermood(wm):
    DatabaseManager.delete_weathermood(wm)


def generate_wm_menu(wm, parent_menu):
    wm_menu = ConsoleMenu(f"{wm.display_string()}", exit_option_text='Go Back')
    wm_menu.append_item(FunctionItem("Open Link", wm.open_link))
    wm_menu.append_item(FunctionItem("Toggle Favorite/Non-favorite", toggle_favorite, args=[wm]))
    wm_menu.append_item(FunctionItem("Delete This Weathermood", delete_weathermood, args=[wm]))
    return SubmenuItem(f"{wm.display_string()}", wm_menu, parent_menu)


def generate_weathermoods_submenu(weathermoods, title, parent_menu):
    submenu = ConsoleMenu(title, exit_option_text=f'Return to {parent_menu.title}')
    for wm in weathermoods:
        wm_submenu_item = generate_wm_menu(wm, submenu)
        submenu.append_item(wm_submenu_item)
    return SubmenuItem(title, submenu, parent_menu)


def get_favorite_weathermoods():
    return DatabaseManager.list_favorite_weathermoods()


def get_all_weathermoods():
    return DatabaseManager.list_all_weathermoods()


def main_menu():
    menu = ConsoleMenu("Main Menu", exit_option_text='Exit')

    # Create New WeatherMood item
    menu.append_item(FunctionItem("Create new", create_new_weathermood))

    # Submenu for Past WeatherMoods
    past_weathermoods_menu = ConsoleMenu("Past WeatherMoods", exit_option_text='Return to Main Menu')

    # Favorites submenu
    favorite_weathermoods = get_favorite_weathermoods()
    favorites_submenu = generate_weathermoods_submenu(favorite_weathermoods, "Favorites", past_weathermoods_menu)
    past_weathermoods_menu.append_item(favorites_submenu)

    # All objects submenu
    all_weathermoods = get_all_weathermoods()
    all_submenu = generate_weathermoods_submenu(all_weathermoods, "All", past_weathermoods_menu)
    past_weathermoods_menu.append_item(all_submenu)

    menu.append_item(SubmenuItem("Past WeatherMoods", past_weathermoods_menu, menu))

    menu.show()



if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,
                        filename='app.log',  # file name
                        filemode='w',  # 'a' for append, 'w' for overwrite
                        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    main_menu()
