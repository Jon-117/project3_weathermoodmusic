"""
Classes for the weather mood project.

Weather, Location, WeatherMood, Menu, Playlist
"""
from dataclasses import dataclass


class Playlist:

    def __init__(self, song_count, title, url, image_link):
        self.song_count = song_count
        self.title = title
        self.url = url
        self.image_url = image_link # Link to the playlist image - Useful when flask is implemented

    def pretty_string(self):
        return f'{self.title} :: {self.song_count} Songs :: {self.url}'
