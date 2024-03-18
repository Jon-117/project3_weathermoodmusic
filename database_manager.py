import sqlite3
import os
from contextlib import contextmanager
import logging
import ui
from classes import WeatherMood

log = logging.getLogger(__name__)


DB_PATH = 'database/weathermood_library.db'

# Ensure the database directory exists
if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH))


@contextmanager  # easier / cleaner connection
def db_connect():
    """
    Context manager for database connections.
    """
    con = sqlite3.connect(DB_PATH)
    log.debug(f'Connected to database: {DB_PATH}')
    yield con
    log.debug(f'Yield from database: {DB_PATH}')
    # Yields control back to `with` until it finishes, then continues
    # from here when db work is done or exception is raised
    con.close()
    log.debug(f'Closed connection to database: {DB_PATH}')


class DatabaseManager:
    @staticmethod
    def create_table():
        """
        Create table for storing weathermoods.
        """
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS weathermood_library (
                id INTEGER PRIMARY KEY,
                city_name TEXT,
                full_name TEXT,
                latitude FLOAT,
                longitude FLOAT,
                temp FLOAT,
                windspeed FLOAT,
                icon TEXT,
                conditions TEXT,
                song_count INTEGER,
                playlist_title TEXT,
                playlist_image_url TEXT,
                playlist_url TEXT,
                created_datetime DATETIME,
                favorite TINYINT
                );
        '''
        with db_connect() as con:
            log.debug('Creating table weathermood_library')
            con.execute(create_table_sql)
            con.commit()
            log.debug('Committing changes to database')
            con.close()
            log.debug('Created table weathermood_library')

    @staticmethod
    def add_weathermood(weathermood):
        """
         Add a WeatherMood to the database.
         """
        insert_sql = '''
            INSERT INTO weathermood_library (
                city_name, full_name, latitude, longitude, temp, windspeed, 
                icon, conditions, song_count, playlist_title, 
                playlist_image_url, playlist_url, created_datetime, favorite
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        with db_connect() as con:
            log.info(f'Adding WeatherMood object to database: {weathermood.display_string()}')
            cursor = con.cursor()
            log.debug(f'Executing SQL for adding object. SQL: {insert_sql}')
            cursor.execute(insert_sql, (
                weathermood.city_name, weathermood.full_name, weathermood.latitude,
                weathermood.longitude, weathermood.temp, weathermood.windspeed,
                weathermood.icon, weathermood.conditions, weathermood.song_count,
                weathermood.playlist_title, weathermood.playlist_image_url,
                weathermood.playlist_url, weathermood.created_datetime, weathermood.favorite
            ))
            weathermood.id = cursor.lastrowid
            log.debug(f'Assigned {weathermood.id} to weathermood {weathermood.display_string()}')
            con.commit()
            con.close()

    @staticmethod
    def delete_weathermood(weathermood):
        """
        Delete weathermood from the database
        """
        log.debug(f'Deleting weathermood: {weathermood}')
        delete_sql = f'DELETE FROM weathermood_library WHERE id = ?'
        with db_connect() as con:
            try:
                cursor = con.cursor()
                log.debug(f'Executing SQL for deleting object (id: {weathermood.id}). SQL: {delete_sql}')
                cursor.execute(delete_sql, (weathermood.id,))
                con.commit()
                con.close()

            except sqlite3.Error as e:
                ui.show_message(f'Error deleting weathermood: \n{e}')

    @staticmethod
    def list_all_weathermoods():
        """
        List all WeatherMoods.
        """
        select_all_sql = 'SELECT * FROM weathermood_library'
        with db_connect() as con:
            con.row_factory = sqlite3.Row
            cursor = con.execute(select_all_sql)
            all_wm = []
            for row in cursor.fetchall():
                wm = DatabaseManager.row_to_weathermood(row)
                all_wm.append(wm)
            return all_wm

    @staticmethod
    def list_favorite_weathermoods():
        """
        List WeatherMoods  that are marked as favorites.
        """
        select_favorites_sql = 'SELECT * FROM weathermood_library WHERE favorite = 1'
        with db_connect() as con:
            con.row_factory = sqlite3.Row
            cursor = con.execute(select_favorites_sql)
            favorites = []
            for row in cursor.fetchall():
                wm = DatabaseManager.row_to_weathermood(row)
                favorites.append(wm)
            return favorites

    @staticmethod
    def row_to_weathermood(row):
        """
        Convert a db row object to a WeatherMood
        """

        log.debug(f'Creating WeatherMood object from row with id {row["id"]}')
        return WeatherMood(
            # WeatherMood Specific
            id=row['id'],
            favorite=bool(row['favorite']),
            created_datetime=row['created_datetime'],
            # Location derived
            city_name=row['city_name'],
            full_name=row['full_name'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            # Weather derived
            temp=row['temp'],
            windspeed=row['windspeed'],
            icon=row['icon'],
            conditions=row['conditions'],
            # Playlist derived
            song_count=row['song_count'],
            playlist_title=row['playlist_title'],
            playlist_image_url=row['playlist_image_url'],
            playlist_url=row['playlist_url']
        )

    @staticmethod
    def toggle_favorite(weathermood):
        """
        Toggle the favorite status of a WeatherMood
        """
        update_sql = '''
            UPDATE weathermood_library
            SET favorite = NOT favorite
            WHERE id = ?
        '''
        with db_connect() as con:
            try:
                con.execute(update_sql, (weathermood.id,))
                con.commit()
                con.close()
            except sqlite3.Error as e:
                ui.alert(f'Error toggling favorite: \n{e}')

# Create table when module is imported... if it doesn't already exist.
# DatabaseManager.create_table()
