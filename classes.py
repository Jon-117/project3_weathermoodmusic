"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass
import sqlite3
import os
from datetime import datetime


folder = 'database'
file = 'weatherMood_library.db'

db = os.path.join(folder, file)

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

    def __init__(self, song_count, playlist_title, playlist_url, playlist_image_url):
        self.song_count = song_count
        self.playlist_title = playlist_title
        self.playlist_url = playlist_url
        self.playlist_image_url = playlist_image_url # Link to the playlist image - Useful when flask is implemented

    def pretty_string(self):
        return f'{self.title} :: {self.song_count} Songs :: {self.url}'
    # Methods for playlist interaction could be added here


class Location:
    def __init__(self, city_name, full_name, latitude, longitude):
        self.city_name = city_name
        self.full_name = full_name
        self.latitude = latitude
        self.longitude = longitude
    # Create method to display location like Playlist class.


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

        self.weathermoodlibrary = WeatherMoodLibrary()

    def display_string(self) -> str:
        display_string = f"{self.conditions.title()} in {self.city_name}... {self.playlist_title}: {self.playlist_url}"
        return display_string
    
    def delete(self): 
        """ Can't delete without the 'self' from this class """
        self.weathermoodlibrary.delete_playlist(self)


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
            created_datetime   = None,

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
            create_table_sql = 'CREATE TABLE IF NOT EXISTS weatherMood_library (city_name TEXT, full_name TEXT, latitude FLOAT, longitude FLOAT, temp FLOAT, windspeed FLOAT, icon TEXT, conditions TEXT, song_count TEXT, playlist_title TEXT, playlist_image_url TEXT, playlist_url TEXT, created_datetime DATETIME, favorite TINYINT, UNIQUE( full_name COLLATE NOCASE, conditions COLLATE NOCASE ))'
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
                    weatherMood.favorite = 0

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
                    r['city_name'],r['full_name'],
                    r['latitude'], r['longitude'],
                    r['temp'], r['windspeed'], 
                    r['icon'],r['conditions'],
                    r['song_count'], r['playlist_title'],
                    r['playlist_image_url'], r['playlist_url'] )
                playlists.append(playlist)

            con.close()

            return playlists
        
        def display_favorites(self, favorite):
            select_favorites_sql = 'SELECT favorite FROM weatherMood_library WHERE favorite = ?'
            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            fav_rows = con.execute(select_favorites_sql, (favorite, ))
            fav_playlists = []

            for r in fav_rows:
                playlist = WeatherMoodLibrary(r['playlist_title'], r['full_name'], r['condition'], r['playlist_url'])
                fav_playlists.append(playlist)
            con.close()

            return fav_playlists

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


# def main():
    

# main()
#Reference for adding data to the database. Also found in 'database_testing'.
# def main():
#     place = Location('austin', 'austin, tx', '23.22','-32.24')
#     playlist = Playlist('3', 'Country', 'https://UrlOfImage.com','https://WeatherMood.com')
#     weather = Weather('9.9', '12.2', 'https://NotImage.com', 'Thunderstorm')

#     builder = WeatherMoodBuilder()
#     compiled_data= builder.build(place, weather, playlist)
#     library = WeatherMoodLibrary()
#     library.add_playlist(compiled_data)
   
# main()

