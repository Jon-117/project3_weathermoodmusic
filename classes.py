"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass
from datetime import datetime
import webbrowser


class Menu:
    def __init__(self, title: str, message: str, options=None):
        self.title = title
        self.message = message
        self.options = options or {}

    def add_option(self, option_name: str, option_function, *args, **kwargs):
        """
        Adds options to the menu's dictionary of option functions. Lambda functions are used to preconfigure the
        functions with params so the functions are not called immediately upon creation of the menu items.

        Note that options showing only strings should still be called this way.

        WeatherMood objects should be shown using ui.show_message"""
        option_name = option_name.title()
        option_function = option_function
        self.options[option_name] = lambda: option_function(*args, **kwargs)

    def remove_option(self, option_name: str):
        try:
            if option_name in self.options.keys():
                del self.options[option_name]
        except KeyError:
            print(f'{option_name} is not a valid option. Ensure the option is spelled exactly as it appears.')
        except Exception as e:
            print(f'{e}')


# TODO - Make a MenuBuilder class
class MenuBuilder:
    def build(self, title: str, subtitle: str, options: dict or list):
        menu = Menu()


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

    def format_time(self, time)-> str:
        return time.strftime("%B %d, %Y - %I:%M %p")


    def display_string(self) -> str:
        """Moderately format the output string. Contains ugly URL """
        new_string = f"{self.conditions.title()} in {self.city_name}. {self.playlist_title}: {self.playlist_url}"
        return new_string

    def pretty_string(self) -> str:
        """Pretty string that doesn't have the URL. Use for the option_name when applying the
        Weathermood.open_link() function to a Menu option"""
        conditions = self.conditions
        city_name = self.city_name
        formatted_time = self.format_time(self.created_datetime)
        playlist = self.playlist_title

        new_string = (f"{formatted_time}... {conditions} in {city_name}. Listening to "
                      f"{playlist}")
        return new_string

    def open_link(self):
        webbrowser.open(self.playlist_url)


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
        id=None,  # Set after storage in db
        favorite=None,  # Set after storage in db
        created_datetime=datetime.now(),  # Set automatically on build
        city_name=city_name,
        full_name=full_name,
        latitude=latitude,
        longitude=longitude,
        temp=temp,
        windspeed=windspeed,
        icon=icon,
        conditions=conditions,
        song_count=song_count,
        playlist_title=playlist_title,
        playlist_image_url=playlist_image_url,
        playlist_url=playlist_url
    )
