def test_delete_all(self):
        builder = WeatherMoodBuilder()
        library = WeatherMoodLibrary()

        # location = Location('Minneapolis', 'Minneapolis, MN', '-22.33','12.24')
        # weather = Weather('45.03', '12.02', 'Getimages.com', 'Rainbow')
        # playlist = Playlist('9', 'Kinetic Disco', 'https://Sometimes.com', 'https://WeatherMood.com')

        # location2 = Location('Austin', 'Austin, TX', '10.33','-23.24')
        # weather2 = Weather('16.00', '15.39', 'https://something.com', 'Sunny')
        # playlist2 = Playlist('12', 'Rock n Pop', 'https://somethingWeird.com', 'https://weatherMood.com')

        # object = builder.build(location, weather, playlist)
        # object2 = builder.build(location2, weather2, playlist2) 

        # library.add_playlist(object)
        # library.add_playlist(object2)

        self.clear_database()