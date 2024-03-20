"""
Weathermood: A vehicle for nostalgia
"""
import classes
import get_location_api
import ui
from classes import WeatherMood, build_weathermood_object
from get_location_api import get_location, LocationError
from get_weather_forcast_api import get_weather_forecast
from get_spotify_api import search_spotify_playlists
from consolemenu import *
from consolemenu.items import *
import database_manager
from database_manager import DatabaseManager
import logging as log


def refreshable_menu(func):
    def wrapper(*args, **kwargs):
        menu = func(*args, **kwargs)  # Generate the menu
        menu.show()  # Display the newly generated menu

    return wrapper


def create_new_weathermood():
    """
    Create a new weathermood. Main function for creating a new weathermood, tying all api together.
    """
    log.info('Creating a new weathermood...')
    location_attempt = 0
    location_success = False
    while True:
        if location_attempt >= 3:
            log.info('Getting location failed. Exiting create_new_weathermood()...')
            break
        location_attempt += 1
        log.debug(f'Attempt #{location_attempt} to get location...')
        try:
            user_city = ""
            while user_city == "":
                user_city = ui.get_user_input("\nWhat city are you in?  ")

            log.debug(f'Calling get_location({user_city})')
            location = get_location(user_city)
            log.info(f'Location object created: {location.city_name}: {location.latitude}, {location.longitude}')
            location_success = True
            break
        except Exception as e:
            log.debug(f'get_location({user_city}) failed! \n{e}\nTrying to get a new city from user attempt {location_attempt} ')
            continue
    if location_success:
        try:
            user_mood = ""
            while user_mood == "":
                user_mood = ui.get_user_input("\nWhat's your mood?  ")
            log.debug(f'User inputs received...\n    City: {user_city}\n    Mood: {user_mood}')
            weather = get_weather_forecast(location.latitude, location.longitude)
            spotify_query = f'{user_mood} {weather.conditions} {location.city_name}'

            playlist = search_spotify_playlists(spotify_query)

            weather_mood = build_weathermood_object(location, weather, playlist)
            weather_mood.open_link()
            DatabaseManager.add_weathermood(weather_mood)
            log.info(weather_mood.weather_mood_object_string())
        except Exception as e:
            error_message = f'Something went wrong. You can try again. '
            log.error(e)
            log.debug(f'Showing error message to user: {error_message}')
            ui.alert(error_message)
    else:
        ui.get_user_input('\nLocation not found. Press enter to return to main menu...  ')



def toggle_favorite(wm):
    DatabaseManager.toggle_favorite(wm)


def delete_weathermood(wm):
    DatabaseManager.delete_weathermood(wm)
    return f'Deleted weathermood: {wm.display_string()}'


def generate_weathermood_menu(wm, parent_menu):
    def submenu_func():
        wm_menu = ConsoleMenu(f"{wm.display_string()}", exit_option_text='Go Back')
        wm_menu.append_item(FunctionItem("Open Link", wm.open_link))
        wm_menu.append_item(FunctionItem("Toggle Favorite/Non-favorite", toggle_favorite, args=[wm]))
        wm_menu.append_item(FunctionItem("Delete This Weathermood", delete_weathermood, args=[wm]))

        wm_menu.show()

    return FunctionItem(f"{wm.display_string()}", submenu_func)


def generate_weathermoods_submenu(db_call_func, title, parent_menu):
    log.debug("Generating weathermood submenus... ")

    def submenu_func():
        submenu = ConsoleMenu(title, exit_option_text=f'Return to {parent_menu.title}')
        weathermoods = db_call_func()
        for weathermood in weathermoods:
            weathermood_submenu_item = generate_weathermood_menu(weathermood, submenu)
            submenu.append_item(weathermood_submenu_item)
        submenu.show()

    return FunctionItem(title, submenu_func, menu=parent_menu)


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
    favorites_submenu = generate_weathermoods_submenu(get_favorite_weathermoods, "Favorites", past_weathermoods_menu)
    past_weathermoods_menu.append_item(favorites_submenu)

    # All objects submenu
    all_submenu = generate_weathermoods_submenu(get_all_weathermoods, "All", past_weathermoods_menu)
    past_weathermoods_menu.append_item(all_submenu)

    menu.append_item(SubmenuItem("Past WeatherMoods", past_weathermoods_menu, menu))

    menu.show()


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,
                    filename='app.log',  # file name
                    filemode='w',  # 'a' for append, 'w' for overwrite
                    format='%(asctime)s - %(module)s - %(levelname)s - Line %(lineno)d: %(message)s')
    # Set-up DB
    database_manager.DatabaseManager.create_table()
    main_menu()
