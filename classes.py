"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist

"""
from dataclasses import dataclass
import sqlite3
import os

db = os.path.join('database', 'playlists.db')

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
    def __init__(self, windspeed, icon, conditions, temp):
        self.windspeed = windspeed
        self.icon = icon  # Icon related to weather conditions. Many freely available.
        self.conditions = conditions # Weather conditions
        self.temp = temp
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

    def __init__(self, location: Location, weather: Weather, playlist: Playlist, id=None, favorite=False):
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
        self.playlist_image_url  = self.playlist.image_url
        self.playlist_url        = self.playlist.url

        self.id                  = id
        self.favorite            = favorite

        self.playlistLibrary     = PlaylistLibrary()

    def save(self):
        self.playlistLibrary.add_playlist(self)
    
    def delete(self):
        self.playlistLibrary.delete_all_playlists(self)
    
        
        


class PlaylistLibrary:
    """ What functions are necessary?
            - Display favorites
            - Display All
            - Add playlist/weatherMood
            - Delete row for favorites only since there is a part in 'add_playlist' that should delete excess rows
        """
    instance = None

    class __PlaylistLibrary:

        def __init__(self):
            create_table_sql = 'CREATE TABLE IF NOT EXISTS playlists (city_name TEXT, full_name TEXT, temp FLOAT, windspeed FLOAT, icon TEXT, conditions TEXT, song_count TEXT, playlist_title TEXT, playlist_image_url TEXT, playlist_url TEXT, favorite BOOLEAN)'
            # Icon will be set as text assuming we save a url or filepath

            con = sqlite3.connect(db)

            with con:
                con.execute(create_table_sql)

            con.close()
        
        # We need to create a database entry when a link is accessed
        def add_playlist(self, weatherMood):
            insert_sql = 'INSERT INTO playlists (city_name, full_name, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, favorite) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            try:
                with sqlite3.connect(db) as con:
                    res = con.execute(insert_sql, (weatherMood.city_name, weatherMood.full_name, weatherMood.temp, weatherMood.windspeed, weatherMood.icon, weatherMood.conditions, weatherMood.song_count, weatherMood.playlist_title, weatherMood.playlist_image_url, weatherMood.playlist_url, weatherMood.favorite))
                    new_id = res.lastrowid # Get the ID of the new row in the table
                    weatherMood.id = new_id

                # The below code should delete rows if it exceeds a certain amount
                cursor = con.cursor()
                cursor.execute('SELECT COUNT(*) FROM playlists') 
                total_row = cursor.fetchone()[0]

                if total_row > 10: 
                    excess_row = total_row - 10 # Finds out how many rows are excess
                    delete_excess_rows = 'DELETE FROM playlists WHERE id IN (SELECT id FROM pllaylists ORDER BY id LIMIT ?)'
                    with sqlite3.connect(db) as con:
                        con.execute(delete_excess_rows, (excess_row))

            except sqlite3.IntegrityError as e:
                raise PlaylistErrors(f'Error - this weather mood already exists. {weatherMood}') from e
            finally:
                con.close()
        

        def delete_playlist(self, weatherMood):
            if not weatherMood.id:
                raise PlaylistErrors(f'id does not exist')

            delete_sql = 'DELETE FROM playlists WHERE rowid = ?'

            with sqlite3.connect(db) as con:
                deleted = con.execute(delete_sql, (id, ))
                deleted_count = deleted.rowcount
            con.close()

            if deleted_count == 0:
                raise PlaylistErrors(f'Could not find the id. Deletion could not occur.')

        def delete_all_playlists(self):
            delete_all_sql = 'DELETE FROM playlists'

            with sqlite3.connect(db) as con:
                deleted = con.execute(delete_all_sql)
            con.close()

        def list_all_playlists(self):
            """ Fetches a limited amount of playlist rows."""
            get_playlists_sql = 'SELECT rowid, * FROM playlists LIMIT 10'
            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            rows = con.execute(get_playlists_sql)
            playlists = []

            for r in rows:
                playlist = PlaylistLibrary(r['playlist_title'], r['full_name'], r['condition'], r['playlist_url'])
                playlists.append(playlist)

            con.close()

            return playlists
        
        def display_favorites(self, read):
            select_favorites_sql = 'SELECT favorite FROM playlist WHERE favorite = ?'
            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            fav_rows = con.execute(select_favorites_sql, (read, ))
            fav_playlists = []

            for r in fav_rows:
                playlist = PlaylistLibrary(r['playlist_title'], r['full_name'], r['condition'], r['playlist_url'])
                fav_playlists.append(playlist)
            con.close()

            return fav_playlists

        def get_playlist_by_id(self, id):
            get_playlist_id_sql = 'SELECT rowid, * FROM playlists WHERE rowid = ?'

            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            rows = con.execute(get_playlist_id_sql, (id, ))
            playlist_data = rows.fetchone()

            if playlist_data:
                playlist = WeatherMood(playlist_data['location: Location'], playlist_data['weather: Weather'], playlist_data['playlist: Playlist'], playlist_data['id'], playlist_data['favorite'])
            con.close()    
            return playlist

    def __new__(cls):
        if not PlaylistLibrary.instance:
            PlaylistLibrary.instance = PlaylistLibrary.__PlaylistLibrary()
        return PlaylistLibrary.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

class PlaylistErrors(Exception):
    """ For errors """
    pass