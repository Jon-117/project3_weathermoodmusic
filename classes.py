"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass
import sqlite3
import os
from datetime import datetime
import webbrowser

if not os.path.exists('database'):
    os.makedirs('database')
file = 'weatherMood_library.db'
db = os.path.join('database', file)

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
        self.id = id
        self.favorite = favorite
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

        self.weathermoodlibrary = WeatherMoodLibrary()

    def add(self):
        if self.id == True:
            self.weathermoodlibrary.update_favorite_weatherMood(self)
        else:
            self.weathermoodlibrary.add_playlist(self)

    def delete(self):
        """ Can't delete without the 'self' from this class """
        self.weathermoodlibrary.delete_playlist(self)

    def format_time(self, time) -> str:
        return datetime.fromtimestamp(time).strftime("%B %d, %Y - %I:%M %p")

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


# ALL BELOW (and db info above) SHOULD BE MOVED TO A NEW DB_MANAGER MODULE
class WeatherMoodLibrary:
    """ What functions are necessary?
            - Display favorites
            - Display All
            - Add playlist/weatherMood
            - Delete row for favorites only since there is a part in 'add_playlist' that should delete excess rows
        """
    instance = None

    class __WeatherMoodLibrary:

        def __init__(self):
            create_table_sql = 'CREATE TABLE IF NOT EXISTS weatherMood_library (city_name TEXT, full_name TEXT, latitude FLOAT, longitude FLOAT, temp FLOAT, windspeed FLOAT, icon TEXT, conditions TEXT, song_count TEXT, playlist_title TEXT, playlist_image_url TEXT, playlist_url TEXT, created_datetime DATETIME, favorite BOOLEAN, UNIQUE( full_name COLLATE NOCASE, playlist_url COLLATE NOCASE ))'
            # Icon will be set as text assuming we save a url or filepath

            con = sqlite3.connect(db)

            with con:
                con.execute(create_table_sql)

            con.close()

        # We need to create a database entry when a link is accessed
        def add_playlist(self, weatherMood):
            insert_sql = 'INSERT INTO weatherMood_library (city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            try:
                with sqlite3.connect(db) as con:
                    res = con.execute(insert_sql, (weatherMood.city_name, weatherMood.full_name, weatherMood.latitude, weatherMood.longitude, weatherMood.temp, weatherMood.windspeed, weatherMood.icon, weatherMood.conditions, weatherMood.song_count, weatherMood.playlist_title, weatherMood.playlist_image_url, weatherMood.playlist_url, weatherMood.created_datetime, weatherMood.favorite))
                    new_id = res.lastrowid # Get the ID of the new row in the table
                    weatherMood.id = new_id

                # The below code should delete rows if it exceeds a certain amount
                cursor = con.cursor()
                cursor.execute('SELECT COUNT(*) FROM weatherMood_library')
                total_row = cursor.fetchone()[0]

                if total_row > 10:
                    excess_row = total_row - 10 # Finds out how many rows are excess
                    delete_rows = excess_row
                    delete_excess_rows = 'DELETE FROM weatherMood_library WHERE rowid IN (SELECT rowid FROM weatherMood_library LIMIT ?)'
                    with sqlite3.connect(db) as con:
                        con.execute(delete_excess_rows, (delete_rows,))

            except sqlite3.IntegrityError as e:
                raise WeatherMoodErrors(f'Error - this weather mood already exists. {weatherMood}') from e
            finally:
                con.close()

        def delete_playlist(self, weatherMood):

            if not weatherMood.id:
                raise WeatherMoodErrors(f'id does not exist')

            delete_sql = 'DELETE FROM weatherMood_library WHERE rowid = ?'

            with sqlite3.connect(db) as con:
                deleted = con.execute(delete_sql, (weatherMood.id, ))
                deleted_count = deleted.rowcount

            if deleted_count == 0:
                raise WeatherMoodErrors(f'Could not find the id. Deletion could not occur.')

        def update_favorite_weatherMood(self, weatherMood):

            if not weatherMood.id:
                raise WeatherMoodErrors(f'id does not exist')

            update_favorite_sql = 'Update weatherMood_library SET favorite = ? WHERE rowid = ?'

            with sqlite3.connect(db) as con:
                update = con.execute(update_favorite_sql, (weatherMood.favorite, weatherMood.id))
                rows_changed = update.rowcount

            if rows_changed == 0:
                raise WeatherMoodErrors(f'WeatherMood id not found')

        def delete_all_playlists(self):
            delete_all_sql = 'DELETE FROM weatherMood_library'

            with sqlite3.connect(db) as con:
                deleted = con.execute(delete_all_sql)
            con.close()

        def list_all_playlists(self):
            """ Fetches a limited amount of weather mood rows."""
            get_playlists_sql = 'SELECT rowid, * FROM weatherMood_library LIMIT 10'
            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            rows = con.execute(get_playlists_sql)
            playlists = []

            for r in rows:
                playlist = WeatherMood(r['rowid'],
                    r['favorite'], r['created_datetime'],
                    r['city_name'], r['full_name'],
                    r['latitude'], r['longitude'],
                    r['temp'], r['windspeed'],
                    r['icon'], r['conditions'],
                    r['song_count'], r['playlist_title'],
                    r['playlist_image_url'], r['playlist_url'] )
                playlists.append(playlist)

            con.close()

            return playlists

        def display_favorites(self, fav):

            select_favorites_sql = 'SELECT rowid, * FROM weatherMood_library WHERE favorite = ?'

            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            fav_rows = con.execute(select_favorites_sql, (fav, ))
            fav_playlists = []

            for r in fav_rows:
                playlist = WeatherMood(r['rowid'],
                    r['favorite'], r['created_datetime'],
                    r['city_name'],r['full_name'],
                    r['latitude'], r['longitude'],
                    r['temp'], r['windspeed'],
                    r['icon'],r['conditions'],
                    r['song_count'], r['playlist_title'],
                    r['playlist_image_url'], r['playlist_url'])
                fav_playlists.append(playlist)
            con.close()

            return fav_playlists

        def num_of_weatherMoods(self):

            num_of_weatherMoods_sql = 'SELECT COUNT(*) FROM weatherMood_library'

            con = sqlite3.connect(db)
            num = con.execute(num_of_weatherMoods_sql)
            count = num.fetchone()[0]

            return count

        def get_playlist_by_id(self, id):

            get_playlist_id_sql = 'SELECT rowid, * FROM weatherMood_library WHERE rowid = ?'

            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            rows = con.execute(get_playlist_id_sql, (id, ))
            playlist_data = rows.fetchone()
            playlist = None

            if playlist_data:
                playlist = WeatherMood(
                    playlist_data['rowid'],
                    playlist_data['favorite'], playlist_data['created_datetime'],
                    playlist_data['city_name'],playlist_data['full_name'],
                    playlist_data['latitude'], playlist_data['longitude'],
                    playlist_data['temp'], playlist_data['windspeed'],
                    playlist_data['icon'],playlist_data['conditions'],
                    playlist_data['song_count'], playlist_data['playlist_title'],
                    playlist_data['playlist_image_url'], playlist_data['playlist_url']
                 )
            con.close()
            return playlist

    def __new__(cls):
        if not WeatherMoodLibrary.instance:
            WeatherMoodLibrary.instance = WeatherMoodLibrary.__WeatherMoodLibrary()
        return WeatherMoodLibrary.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

class WeatherMoodErrors(Exception):
    """ For errors """
    pass



