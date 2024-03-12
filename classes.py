"""
Classes for the weather mood project.

Weather, Location, WeatherMood
"""
from dataclasses import dataclass
from datetime import datetime


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
    song_count: int  # Number of songs in the playlist
    title: str  # Title of the playlist
    url: str  # URL to access the playlist
    image_link: str  # Link to the playlist image

    # Methods for playlist interaction could be added here


class Location:
    def __init__(self, city_name, full_name, latitude, longitude):
        self.city_name = city_name
        self.full_name = full_name
        self.lat = latitude
        self.lon = longitude


class WeatherMood:
    """
    WeatherMood class stores the reminiscence
    """
    def __init__(self,
                 id, favorite, created_datetime,
                 city_name, full_name, latitude, longitude,
                 temp, windspeed, icon, conditions,
                 song_count, playlist_title, playlist_image_url, playlist_url):

        # WeatherMood Specific
        self.id = None
        self.favorite = False
        self.created_datetime = created_datetime if created_datetime else datetime.now()   # Date created. Doesn't change if it's supplied (ie, when recreating object from db)
        # Location derived
        self.city_name = city_name
        self.full_name = full_name
        self.latitude = latitude
        self.longitude = longitude
        # Weather derived
        self.temp = temp
        self.windspeed = windspeed
        self.icon = icon
        self.conditions = conditions
        # Playlist derived
        self.song_count = song_count
        self.playlist_title = playlist_title
        self.playlist_image_url = playlist_image_url
        self.playlist_url = playlist_url

        def display_string() -> str:
            display_string = f"{conditions.title()} in {self.city_name}... {playlist_title}: {playlist_url}"
            return display_string


class WeatherMoodBuilder:
    def build(self, location, weather, playlist):
        # Extracting information from the Location object
        city_name = location.city_name
        full_name = location.full_name
        latitude = location.latitude
        longitude = location.longitude

        # Extracting information from the Weather object
        temp = weather.temp
        windspeed = weather.windspeed
        icon = weather.icon
        conditions = weather.conditions

        # Extracting information from the Playlist object
        song_count = playlist.song_count
        playlist_title = playlist.playlist_title
        playlist_image_url = playlist.playlist_image_url
        playlist_url = playlist.playlist_url

        # Building and returning the WeatherMood object
        return WeatherMood(
            id                 = None, # Set after storage in db
            favorite           = None, # Set after storage in db
            city_name          = city_name,
            full_name          = full_name,
            latitude           = latitude,
            longitude          = longitude,
            temp               = temp,
            windspeed          = windspeed,
            icon               = icon,
            conditions         = conditions,
            song_count         = song_count,
            playlist_title     = playlist_title,
            playlist_image_url = playlist_image_url,
            playlist_url       = playlist_url
        )
