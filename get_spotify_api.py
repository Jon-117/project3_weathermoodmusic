"""
Handles api calls to spotify for playlists.
"""
import pprint

from classes import Playlist
import requests
import os
from random import randint

# credentials from the Spotify Developer Dashboard
client_id = os.environ.get('SPOTIFY_WEB_DEV_WEATHERMOOD_ID')
client_secret = os.environ.get('SPOTIFY_WEB_DEV_WEATHERMOOD_SECRET')


# Obtain an access token - necessary to access api
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    if auth_response.status_code == 200:
        return auth_response.json()['access_token']
    else:
        return None


def spotify_api_request(query, access_token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': query,
        'type': 'playlist',
        'limit': 10  # Adjust the number of results as needed
    }

    response = requests.get(search_url, headers=headers, params=params)
    return response.json()


def search_spotify_playlists(query) -> Playlist:
    access_token = get_access_token(client_id, client_secret)
    if access_token:

        results = spotify_api_request(query, access_token)
        playlist_list = []
        for playlist in results['playlists']['items']:
            link = playlist['external_urls']['spotify']
            title = playlist['name']
            song_count = int(playlist["tracks"]["total"])
            image_link = playlist['images'][0]['url']

            new_playlist = Playlist(song_count, title, link, image_link)
            playlist_list.append(new_playlist)
            # print(new_playlist.pretty_string())
        random_pick = randint(0, len(playlist_list) - 1)
        random_playlist = playlist_list[random_pick]
        return random_playlist

    else:
        print('Failed to retrieve access token')

