"""
Weathermood: A vehicle for nostalgia
"""

import ui
from classes import Menu, MenuBuilder, Weather, WeatherMood, build_weathermood_object, Location, Playlist
from get_location import get_location
from getWeatherForecast import get_weather_forecast
from spotify_api import search_spotify_playlists


def create_new_weathermood(): # Functionally works, just need DB connection to store new WM objects.
    """
    Create a new weathermood. Main function for creating a new weathermood, tying all api together.
    """
    user_city = ui.get_user_input("What city are you in?  ")
    user_mood = ui.get_user_input("What's your mood?  ")
    location = get_location(user_city)
    weather = get_weather_forecast(location.latitude, location.longitude)
    spotify_query = f'{user_mood} {weather.conditions} {location.city_name}'

    playlist = search_spotify_playlists(spotify_query)
    # print(isinstance(playlist, Playlist))

    weather_mood = build_weathermood_object(location, weather, playlist)
    weather_mood.open_link()
    # TODO - Store the object in database
    print(weather_mood.pretty_string())
    return weather_mood


main_menu_options = {
    "Create a new Weathermood": create_new_weathermood,

}
menu = MenuBuilder.build('Weathermood: A vehicle for nostalgia', 'Main Menu', main_menu_options)
