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
    def setUpClass(cls):
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

    def add_playlist2(self):
        builder = WeatherMoodBuilder()
        library = WeatherMoodLibrary()
        
        location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        object = builder.build(location, weather, playlist) # builder extracts data from api classes and gives it to the WeatherMood class
        
        library.add_playlist(object)


    def test_add_fifteen_playlists(self):  
        # saves 15 different objects and asserts total rows = 10. The database add function prevents more than 10 rows of records.
        self.clear_database()
        builder = WeatherMoodBuilder()
        library = WeatherMoodLibrary()
        
        location1 = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather1 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist1 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location2 = Location('New York City', 'New York City, NY', '-22.33','12.24')
        weather2 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist2 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location3 = Location('Los Angeles', 'Los Angeles, CA', '-22.33','12.24')
        weather3 = Weather('45.03', '12.02', 'Getimages.com', 'sunny')
        playlist3 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location4 = Location('Houston', 'Houston, TX', '-22.33','12.24')
        weather4 = Weather('45.03', '12.02', 'Getimages.com', 'rainy')
        playlist4 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location5 = Location('Phoenix', 'Phoenix, AZ', '-22.33','12.24')
        weather5 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist5 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location6 = Location('Philadelphia', 'Philadelphia, PA', '-22.33','12.24')
        weather6 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist6 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location7 = Location('San Antonio', 'San Antonio, TX', '-22.33','12.24')
        weather7 = Weather('45.03', '12.02', 'Getimages.com', 'Sunny')
        playlist7 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location8 = Location('San Diego', 'San Diego, CA', '-22.33','12.24')
        weather8 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist8 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location9 = Location('Dallas', 'Dallas, TX', '-22.33','12.24')
        weather9 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist9 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location10 = Location('San Jose', 'San Jose, CA', '-22.33','12.24')
        weather10 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist10 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location11 = Location('Austin', 'Austin, TX', '-22.33','12.24')
        weather11 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist11 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location12 = Location('Jacksonville', 'Jacksonville, FL', '-22.33','12.24')
        weather12 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist12 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location13 = Location('Fort Worth', 'Fort Worth, TX', '-22.33','12.24')
        weather13 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist13 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location14 = Location('Columbus', 'Columbus, OH', '-22.33','12.24')
        weather14 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist14 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location15 = Location('Charlotte', 'Charlotte, NC', '-22.33','12.24')
        weather15 = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist15 = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        object1 = builder.build(location1, weather1, playlist1)
        object2 = builder.build(location2, weather2, playlist2)
        object3 = builder.build(location3, weather3, playlist3)
        object4 = builder.build(location4, weather4, playlist4)
        object5 = builder.build(location5, weather5, playlist5)
        object6 = builder.build(location6, weather6, playlist6)
        object7 = builder.build(location7, weather7, playlist7)
        object8 = builder.build(location8, weather8, playlist8)
        object9 = builder.build(location9, weather9, playlist9)
        object10 = builder.build(location10, weather10, playlist10)
        object11 = builder.build(location11, weather11, playlist11)
        object12 = builder.build(location12, weather12, playlist12)
        object13 = builder.build(location13, weather13, playlist13)
        object14 = builder.build(location14, weather14, playlist14)
        object15 = builder.build(location15, weather15, playlist15)

        library.add_playlist(object1)
        library.add_playlist(object2)
        library.add_playlist(object3)
        library.add_playlist(object4)
        library.add_playlist(object5)
        library.add_playlist(object6)
        library.add_playlist(object7)
        library.add_playlist(object8)
        library.add_playlist(object9)
        library.add_playlist(object10)
        library.add_playlist(object11)
        library.add_playlist(object12)
        library.add_playlist(object13)
        library.add_playlist(object14)
        library.add_playlist(object15)

        self.assertEqual(10, library.num_of_weatherMoods()) # Makes sure there are no more than 10 rows in the table even though 15 were added.

        self.clear_database()

    def test_duplicate_error(self):
        # Makes  
        self.clear_database()   
        self.add_playlist()
        with self.assertRaises(WeatherMoodErrors):
            self.add_playlist()

        self.clear_database()
            
    def test_display_all(self):
        self.clear_database()
        library = WeatherMoodLibrary()
        self.add_playlist()
        self.add_playlist2()
        weatherMoods = library.list_all_playlists()
        
        
        for row in weatherMoods:
            data = row
            city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = data.city_name, data.full_name, data.latitude, data.longitude, data.temp, data.windspeed, data.icon, data.conditions, data.song_count, data.playlist_title, data.playlist_image_url, data.playlist_url, data.created_datetime, data.favorite
            print(f'test_display_all: {city_name}, {full_name}, {latitude}, {longitude} | {temp}, {windspeed}, {icon}, {conditions} | {song_count}, {playlist_title}, {playlist_image_url}, {playlist_url} | {created_datetime}, {favorite}')
        self.clear_database()

    def test_delete_playlist(self):
        # If unittest is ran without 'test_delete_all' it errors after two runs, because it can't properly grab a row.
        self.clear_database()
        self.add_playlist()
        library = WeatherMoodLibrary()
        playlist_id = 1
        returned_data = library.get_playlist_by_id(playlist_id)
        returned_data.delete()

    def test_delete_all(self):
        self.clear_database()
        builder = WeatherMoodBuilder()
        library = WeatherMoodLibrary()

        location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        location2 = Location('Austin', 'Austin, TX', '10.33','-23.24')
        weather2 = Weather('16.00', '15.39', 'https://something.com', 'Sunny')
        playlist2 = Playlist('12', 'Rock n Pop', 'https://somethingWeird.com', 'https://weatherMood.com')

        object = builder.build(location, weather, playlist)
        object2 = builder.build(location2, weather2, playlist2) 

        library.add_playlist(object)
        library.add_playlist(object2)

        self.clear_database()
        
    def test_favorite(self):
        self.clear_database()
        library = WeatherMoodLibrary()

        self.add_playlist()
        self.add_playlist2()
        #______________________________________ Get object and add or update it
        playlist = library.get_playlist_by_id(1)
        playlist.favorite = 1
        playlist.add()
        #_______________________________________ Grab favorite weather_moods
        returned_data = library.display_favorites(True)

        for row in returned_data:
            data = row
            city_name, full_name, latitude, longitude, temp, windspeed, icon, conditions, song_count, playlist_title, playlist_image_url, playlist_url, created_datetime, favorite = data.city_name, data.full_name, data.latitude, data.longitude, data.temp, data.windspeed, data.icon, data.conditions, data.song_count, data.playlist_title, data.playlist_image_url, data.playlist_url, data.created_datetime, data.favorite
            print(f'test_favorite: {city_name}, {full_name}, {latitude}, {longitude} | {temp}, {windspeed}, {icon}, {conditions} | {song_count}, {playlist_title}, {playlist_image_url}, {playlist_url} | {created_datetime}, {favorite}')
        self.clear_database()

    
if __name__ == '__main__':
    unittest.main()