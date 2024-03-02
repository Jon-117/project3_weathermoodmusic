"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass

class Menu:
    #TODO - Fill in the rest of this class
    def __init__(self):
        # Initialize menu options here
        pass

    def add_option(self, option_name, option_function):
        # Code to add menu option
        pass

    def remove_option(self, option_name):
        # Code to remove menu option
        pass


@dataclass
class Weather:
    windspeed: float
    icon: str  # Icon related to weather conditions. Many freely available.
    conditions: str  # Weather conditions
    temp: float
    # Potential methods for interacting with weather APIs


@dataclass 
class Playlist:

    def __init__(self, song_count, title, url, image_link):
        self.song_count = song_count
        self.title = title
        self.url = url
        self.image_url = image_link # Link to the playlist image - Useful when flask is implemented

    def pretty_string(self):
        return f'{self.title} :: {self.song_count} Songs :: {self.url}'
    # Methods for playlist interaction could be added here

class Location:
    # Placeholder for location attributes and methods
    def __init__(self, city_name, full_name):
        self.city_name = city_name
        self.full_name = full_name

    def weather_query_str(self):
        # Method to return a string suitable for searching weather API
        return f'{self.city_name}'  # Better to use a manipulation of full_name?


class WeatherMood:

    def __init__(self, location: Location, weather: Weather, playlist: Playlist):
        self.location            = location
        self.weather             = weather
        self.playlist            = playlist

        self.city_name           = self.location.city_name
        self.full_name           = self.location.full_name

        self.temp                = self.weather.temp
        self.windspeed           = self.weather.windspeed
        self.icon                = self.weather.icon
        self.conditions          = self.weather.conditions

        self.song_count          = self.playlist.song_count
        self.playlist_title      = self.playlist.title
        self.playlist_image_link = self.playlist.image_link
        self.playlist_url        = self.playlist.url

