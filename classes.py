"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass
from datetime import datetime
import webbrowser


@dataclass
class Weather:
    windspeed: float  # Represents the wind speed.
    icon: str  # Represents the icon related to weather conditions.
    conditions: str  # Represents the weather conditions.
    temp: float  # Represents the temperature.


class Playlist:
    def __init__(self, song_count, title, url, image_url):
        self.song_count = song_count
        self.title = title
        self.url = url
        self.image_url = image_url  # Link to the playlist image - Useful when flask is implemented

    def pretty_string(self):
        return f'{self.title} :: {self.song_count} Songs :: {self.url}'


class Location:
    def __init__(self, city_name, full_name, latitude, longitude):
        self.city_name = city_name
        self.full_name = full_name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{self.full_name}'


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
        self.id = id if id else None
        self.favorite = 0  # Always start as non-favorite
        self.created_datetime = created_datetime if created_datetime else datetime.now()  # Date created. Doesn't change if it's supplied (ie, when recreating object from db)
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

    def format_time(self, time) -> str:
        return datetime.fromtimestamp(time).strftime("%B %d, %Y - %I:%M %p")

    def __str__(self):
        return f"ID: {self.id} - {self.conditions.title()} in {self.city_name}: {self.playlist_title}"

    def display_string(self) -> str:
        """Moderately format the output string. Contains ugly URL """
        new_string = f"ID: {self.id} - {self.conditions.title()} in {self.city_name}. {self.playlist_title}: {self.playlist_url}"
        return new_string

    def pretty_string(self) -> str:
        """Pretty string that doesn't have the URL. Use for the option_name when applying the
        Weathermood.open_link() function to a Menu option"""
        conditions = self.conditions
        city_name = self.city_name
        formatted_time = self.format_time(self.created_datetime)
        playlist = self.playlist_title

        new_string = (f"{formatted_time}... {conditions} in {city_name}.\n  Listened to "
                      f"{playlist}")
        return new_string

    def open_link(self):
        webbrowser.open(self.playlist_url)

    def weather_mood_object_string(self) -> str:
        """
        Returns a string that can be used to recreate the weathermood object in a new file. For creating test data
        while the db is unavailable.
        """
        weathermood_object_string = f"WeatherMood({self.id}, {self.favorite}, {self.created_datetime.timestamp()}, '{self.city_name}', '{self.full_name}', {self.latitude}, {self.longitude}, {self.temp}, {self.windspeed}, '{self.icon}', '{self.conditions}', {self.song_count}, '{self.playlist_title}', '{self.playlist_image_url}', '{self.playlist_url}')"
        return weathermood_object_string


def build_weathermood_object(location, weather, playlist):
    """
    Build a Weathermood object from three basic classes location, weather, playlist.
    """
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
    playlist_title = playlist.title
    playlist_image_url = playlist.image_url
    playlist_url = playlist.url

    # Building and returning the WeatherMood object
    return WeatherMood(
        # WeatherMood Specific
        id=None,  # Set after storage in db
        favorite=0,
        created_datetime=datetime.now(),  # Set automatically on build
        # Location Specific
        city_name=city_name,
        full_name=full_name,
        latitude=latitude,
        longitude=longitude,
        # Weather Specific
        temp=temp,
        windspeed=windspeed,
        icon=icon,
        conditions=conditions,
        # Playlist Specific
        song_count=song_count,
        playlist_title=playlist_title,
        playlist_image_url=playlist_image_url,
        playlist_url=playlist_url
    )
