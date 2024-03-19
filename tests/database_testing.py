""" 
This file tests the different methods for querying the database.
Make sure to change your file path to run this. 
"""
import os
import unittest
from unittest import TestCase

import time

import sys
sys.path.append("..") # Necessary to find 'classes' file
import classes
from classes import Weather, Playlist, Location, build_weathermood_object, WeatherMoodLibrary, WeatherMoodErrors


class TestWeatherMood_Library(TestCase):
    
    @classmethod
    def setUpClass(cls):
        classes.db = os.path.join('database', 'TestPlaylists.db')
        WeatherMoodLibrary.instance = None

    def clear_database(self):
        library = WeatherMoodLibrary()
        library.delete_all_playlists()

    def add_playlist(self):
        library = WeatherMoodLibrary()
        
        location = Location('Plymouth', 'Plymouth, MN', '-23.33','32.24')
        weather = Weather('40.00', '10.00', 'Https://icon.com', 'Rainy/Cloudy')
        playlist = Playlist('14', 'Dubstep Boom', 'https://imageurl.com', 'https://playlist.com')
        
        object = build_weathermood_object(location, weather, playlist) # builder extracts data from api classes and gives it to the WeatherMood class
        library.add_playlist(object)

    def add_playlist_2(self):
        library = WeatherMoodLibrary()
        
        location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        object = build_weathermood_object(location, weather, playlist) # builder extracts data from api classes and gives it to the WeatherMood class
        library.add_playlist(object)


    def test_add_fifteen_playlists(self):  
        # saves 15 different objects and asserts total rows = 10. The database add function prevents more than 10 rows of records.
        self.clear_database()
        library = WeatherMoodLibrary()
        
        location_1 = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather_1 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_1 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood1.com')

        location_2 = Location('New York City', 'New York City, NY', '-22.33','12.24')
        weather_2 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_2 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood2.com')

        location_3 = Location('Los Angeles', 'Los Angeles, CA', '-22.33','12.24')
        weather_3 = Weather('45.03', '12.02', 'Getimages.com', 'sunny')
        playlist_3 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood3.com')

        location_4 = Location('Houston', 'Houston, TX', '-22.33','12.24')
        weather_4 = Weather('45.03', '12.02', 'Getimages.com', 'rainy')
        playlist_4 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood4.com')

        location_5 = Location('Phoenix', 'Phoenix, AZ', '-22.33','12.24')
        weather_5 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_5 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood5.com')

        location_6 = Location('Philadelphia', 'Philadelphia, PA', '-22.33','12.24')
        weather_6 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_6 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood6.com')

        location_7 = Location('San Antonio', 'San Antonio, TX', '-22.33','12.24')
        weather_7 = Weather('45.03', '12.02', 'Getimages.com', 'Sunny')
        playlist_7 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood7.com')

        location_8 = Location('San Diego', 'San Diego, CA', '-22.33','12.24')
        weather_8 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_8 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood8.com')

        location_9 = Location('Dallas', 'Dallas, TX', '-22.33','12.24')
        weather_9 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_9 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood9.com')

        location_10 = Location('San Jose', 'San Jose, CA', '-22.33','12.24')
        weather_10 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_10 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood10.com')

        location_11 = Location('Austin', 'Austin, TX', '-22.33','12.24')
        weather_11 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_11 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood11.com')

        location_12 = Location('Jacksonville', 'Jacksonville, FL', '-22.33','12.24')
        weather_12 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_12 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood12.com')

        location_13 = Location('Fort Worth', 'Fort Worth, TX', '-22.33','12.24')
        weather_13 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_13 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood13.com')

        location_14 = Location('Columbus', 'Columbus, OH', '-22.33','12.24')
        weather_14 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_14 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood14.com')

        location_15 = Location('Charlotte', 'Charlotte, NC', '-22.33','12.24')
        weather_15 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist_15 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood15.com')

        # Time sleep() is used because I used datetime as a unique key along with the playlistUrl, because I was getting an integrity error with full_name and conditions
        object_1 = build_weathermood_object(location_1, weather_1, playlist_1)
        time.sleep(1)
        object_2 = build_weathermood_object(location_2, weather_2, playlist_2)
        time.sleep(1)
        object_3 = build_weathermood_object(location_3, weather_3, playlist_3)
        time.sleep(1)
        object_4 = build_weathermood_object(location_4, weather_4, playlist_4)
        time.sleep(1)
        object_5 = build_weathermood_object(location_5, weather_5, playlist_5)
        time.sleep(1)
        object_6 = build_weathermood_object(location_6, weather_6, playlist_6)
        time.sleep(1)
        object_7 = build_weathermood_object(location_7, weather_7, playlist_7)
        time.sleep(1)
        object_8 = build_weathermood_object(location_8, weather_8, playlist_8)
        time.sleep(1)
        object_9 = build_weathermood_object(location_9, weather_9, playlist_9)
        time.sleep(1)
        object_10 = build_weathermood_object(location_10, weather_10, playlist_10)
        time.sleep(1)
        object_11 = build_weathermood_object(location_11, weather_11, playlist_11)
        time.sleep(1)
        object_12 = build_weathermood_object(location_12, weather_12, playlist_12)
        time.sleep(1)
        object_13 = build_weathermood_object(location_13, weather_13, playlist_13)
        time.sleep(1)
        object_14 = build_weathermood_object(location_14, weather_14, playlist_14)
        time.sleep(1)
        object_15 = build_weathermood_object(location_15, weather_15, playlist_15)

        library.add_playlist(object_1)
        library.add_playlist(object_2)
        library.add_playlist(object_3)
        library.add_playlist(object_4)
        library.add_playlist(object_5)
        library.add_playlist(object_6)
        library.add_playlist(object_7)
        library.add_playlist(object_8)
        library.add_playlist(object_9)
        library.add_playlist(object_10)
        library.add_playlist(object_11)
        library.add_playlist(object_12)
        library.add_playlist(object_13)
        library.add_playlist(object_14)
        library.add_playlist(object_15)

        self.assertEqual(10, library.num_of_weatherMoods()) # Makes sure there are no more than 10 rows in the table even though 15 were added.

        self.clear_database()


    def test_duplicate_error(self):
        # Makes duplicates to test if it errors
        self.clear_database()   
        self.add_playlist()
        with self.assertRaises(WeatherMoodErrors):
            self.add_playlist()
        self.clear_database()
            

    def test_display_all(self):
        self.clear_database()
        library = WeatherMoodLibrary()
        self.add_playlist()
        self.add_playlist_2()
        weatherMoods = library.list_all_playlists()
        
        for row in weatherMoods:
            data = row
            city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = data.city_name, data.full_name, data.latitude, data.longitude, data.temp, data.windspeed, data.icon, data.conditions, data.song_count, data.playlist_title, data.playlist_image_url, data.playlist_url, data.created_datetime, data.favorite
            print(f'test_display_all: {city_name}, {full_name}, {latitude}, {longitude} | {temp}, {windspeed}, {icon}, {conditions} | {song_count}, {playlist_title}, {playlist_image_url}, {playlist_url} | {created_datetime}, {favorite}')
        self.clear_database()


    def test_delete_playlist(self):
        self.clear_database()
        self.add_playlist()
        library = WeatherMoodLibrary()
        playlist_id = 1
        returned_data = library.get_playlist_by_id(playlist_id)
        returned_data.delete()


    def test_delete_all(self):
        self.clear_database()
        library = WeatherMoodLibrary()

        location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location_2 = Location('Austin', 'Austin, TX', '10.33','-23.24')
        weather_2 = Weather('16.00', '15.39', 'https://something.com', 'Sunny')
        playlist_2 = Playlist('12', 'Rock n Pop', 'https://somethingWeird.com', 'https://weatherMood.com')

        object = build_weathermood_object(location, weather, playlist)
        object_2 = build_weathermood_object(location_2, weather_2, playlist_2) 

        library.add_playlist(object)
        library.add_playlist(object_2)

        self.clear_database()
        

    def test_favorite(self):
        self.clear_database()
        library = WeatherMoodLibrary()

        self.add_playlist()
        self.add_playlist_2()
        
        #Get object and add or update it
        playlist = library.get_playlist_by_id(1)
        print(playlist.id)
        playlist.favorite = 1
        playlist.add()

        #Grab favorite weather_moods
        returned_data = library.display_favorites(True)

        for row in returned_data:
            data = row
            city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = data.city_name, data.full_name, data.latitude, data.longitude, data.temp, data.windspeed, data.icon, data.conditions, data.song_count, data.playlist_title, data.playlist_image_url, data.playlist_url, data.created_datetime, data.favorite
            print(f'test_favorite: {city_name}, {full_name}, {latitude}, {longitude} | {temp}, {windspeed}, {icon}, {conditions} | {song_count}, {playlist_title}, {playlist_image_url}, {playlist_url} | {created_datetime}, {favorite}')
        self.clear_database()

    
if __name__ == '__main__':
    unittest.main()