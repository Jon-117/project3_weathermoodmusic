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
    windspeed: float  # Represents the wind speed.
    icon: str  # Represents the icon related to weather conditions.
    conditions: str  # Represents the weather conditions.
    temp: float  # Represents the temperature.
    # Potential methods for interacting with weather APIs

    def __init__(self,windspeed,icon,conditions,temp):
        self.windspeed = windspeed
        self.icon = icon
        self.conditions = conditions

    def __str__(self) -> str:
        return f'Windspeed: {self.windspeed}\nIcon: {self.icon}\nConditions: {self.conditions}\nTemperature: {self.temp}'


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
    def __init__(self, city_name, full_name, latitude, longitude):
        self.city_name = city_name
        self.full_name = full_name
        self.lat = latitude
        self.lon = longitude


class WeatherMood:
    def __init__(self, location: Location, weather: Weather, playlist: Playlist):
        self.location = location
        self.weather = weather
        self.playlist = playlist

        self.city_name = self.location.city_name
        self.full_name = self.location.full_name

        self.temp = self.weather.temp
        self.windspeed = self.weather.windspeed
        self.icon = self.weather.icon
        self.conditions = self.weather.conditions

        self.song_count = self.playlist.song_count
        self.playlist_title = self.playlist.title
        self.playlist_image_link = self.playlist.image_url
        self.playlist_url = self.playlist.url

