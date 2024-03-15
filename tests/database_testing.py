""" 
This file tests the different methods for querying the database.
Make sure to change your file path to run this. 
"""
import os
import unittest
from unittest import TestCase

import sys
sys.path.append("..") # Necessary to find 'classes' file
import classes
from classes import Weather, Playlist, Location, WeatherMoodBuilder, WeatherMoodLibrary, WeatherMood, WeatherMoodErrors


class TestWeatherMood_Library(TestCase):
    
    @classmethod
    def prepDatabase():
        from pathlib import Path
        Path("database").mkdir(parents=True, exist_ok=True)

        classes.db = os.path.join('database', 'TestPlaylists.db')
        WeatherMoodLibrary.instance = None
    
    def clear_database(self):
        library = WeatherMoodLibrary()
        library.delete_all_playlists()

    def add_playlist(self):
        builder = WeatherMoodBuilder()
        library = WeatherMoodLibrary()
        
        location = Location('Plymouth', 'Plymouth, MN', '-23.33','32.24')
        weather = Weather('40.00', '10.00', 'Https://icon.com', 'Rainy/Cloudy')
        playlist = Playlist('14', 'Dubstep Boom', 'https://imageurl.com', 'https://playlist.com')

        object = builder.build(location, weather, playlist) # builder extracts data from api classes and gives it to the WeatherMood class
        
        library.add_playlist(object)


    # def test_display_all(self):
    #     library = WeatherMoodLibrary()
    #     self.add_playlist()
    #     weatherMoods = library.list_all_playlists()
    #     data = weatherMoods[0]
    #     city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = data.city_name, data.full_name, data.latitude, data.longitude, data.temp, data.windspeed, data.icon, data.conditions, data.song_count, data.playlist_title, data.playlist_image_url, data.playlist_url, data.created_datetime, data.favorite
    #     print(city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite)
    #     self.clear_database()

    # def test_delete_playlist(self):
    #     # If unittest is ran without 'test_delete_all' it errors after two runs, because it can't properly grab a row.
    #     self.add_playlist()
    #     library = WeatherMoodLibrary()
    #     playlist_id = 1
    #     returned_data = library.get_playlist_by_id(playlist_id)
    #     returned_data.delete()

    # def test_duplicate_error(self):
    #     self.add_playlist()
    #     with self.assertRaises(WeatherMoodErrors):
    #         self.add_playlist()

    #     self.clear_database()

    # def test_delete_all(self):
    #     builder = WeatherMoodBuilder()
    #     library = WeatherMoodLibrary()

    #     location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
    #     weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
    #     playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

    #     location2 = Location('Austin', 'Austin, TX', '10.33','-23.24')
    #     weather2 = Weather('16.00', '15.39', 'https://something.com', 'Sunny')
    #     playlist2 = Playlist('12', 'Rock n Pop', 'https://somethingWeird.com', 'https://weatherMood.com')

    #     object = builder.build(location, weather, playlist)
    #     object2 = builder.build(location2, weather2, playlist2) 

    #     library.add_playlist(object)
    #     library.add_playlist(object2)

    #     self.clear_database()
        
    # def test_favorite(self):
    #     library = WeatherMoodLibrary()

    #     self.add_playlist()
    #     #______________________________________ Get object and add or update it
    #     playlist = library.get_playlist_by_id(1)
    #     playlist.favorite = 1
    #     playlist.add()
    #     #_______________________________________ Grab favorite weather_moods
    #     weather_mood = library.display_favorites()

    #     city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = weather_mood.city_name, weather_mood.full_name, weather_mood.latitude, weather_mood.longitude, weather_mood.temp, weather_mood.windspeed, weather_mood.icon, weather_mood.conditions, weather_mood.song_count, weather_mood.playlist_title, weather_mood.playlist_image_url, weather_mood.playlist_url, weather_mood.created_datetime, weather_mood.favorite
    #     print(city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite)

        # self.clear_database()

    
if __name__ == '__main__':
    TestWeatherMood_Library.prepDatabase()
    unittest.main()