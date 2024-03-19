from classes import WeatherMoodLibrary, build_weathermood_object, Location, Weather, Playlist
library = WeatherMoodLibrary()

location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24') # {city_name, full_name, latitude, longitude}
weather = Weather('45.03', 'Getimages.com', 'Rainbow', '12.02') # {windspeed, icon, conditions, temp}
playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com') # {song_count, title, url, image_url}

location2 = Location('Austin', 'Austin, TX', '10.33','-23.24')
weather2 = Weather('16.00', 'https://something.com', 'Sunny', '15.39')
playlist2 = Playlist('12', 'Rock n Pop', 'https://somethingWeird.com', 'https://weatherMood.com')

object = build_weathermood_object(location, weather, playlist)
object2 = build_weathermood_object(location2, weather2, playlist2) 

library.add_playlist(object)
library.add_playlist(object2)