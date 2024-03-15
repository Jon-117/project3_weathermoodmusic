import requests
from pprint import pprint
import os

# credentials from the Spotify Developer Dashboard
client_id = os.environ.get('SPOTIFY_WEB_DEV_WEATHERMOOD_ID')
client_secret = os.environ.get('SPOTIFY_WEB_DEV_WEATHERMOOD_SECRET')


# Obtain an access token - necessary to access api
def get_access_token(spotify_id, spotify_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': spotify_id,
        'client_secret': spotify_secret,
    })

    if auth_response.status_code == 200:
        return auth_response.json()['access_token']
    else:
        return None


def search_spotify_playlists(query, token):
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'q': query,
        'type': 'playlist',
        'limit': 1  # Adjust the number of results as needed
    }

    response = requests.get(search_url, headers=headers, params=params)
    return response.json()


access_token = get_access_token(client_id, client_secret)
if access_token:
    # ask = input('Enter playlist search term here: ')
    results = search_spotify_playlists('low key warm summer day', access_token)

    for playlist in results['playlists']['items']:
        link = playlist['external_urls']['spotify']
        title = playlist['name']
        song_count = f':: {playlist["tracks"]["total"]} Songs ::'
        print(title, song_count, link)
else:
    print('Failed to retrieve access token')

# pprint(results)

"""
example response data
note that the urls that have api.spotify.com in them require the access token. We don't *need* them, but may add flavor.

{'playlists': {'href': 'https://api.spotify.com/v1/search?query=low+key+warm+summer+day&type=playlist&offset=0&limit=1',
               'items': [{'collaborative': False,
                          'description': 'Relax with these timeless tunes. '
                                         'Cover: Tracy Chapman',
                          'external_urls': {'spotify': 'https://open.spotify.com/playlist/37i9dQZF1DWTQwRw56TKNc'},
                          'href': 'https://api.spotify.com/v1/playlists/37i9dQZF1DWTQwRw56TKNc',
                          'id': '37i9dQZF1DWTQwRw56TKNc',
                          'images': [{'height': None,
                                      'url': 'https://i.scdn.co/image/ab67706f000000032733cec565637f3ff0fd0de9',
                                      'width': None}],
                          'name': 'Mellow Classics',
                          'owner': {'display_name': 'Spotify',
                                    'external_urls': {'spotify': 'https://open.spotify.com/user/spotify'},
                                    'href': 'https://api.spotify.com/v1/users/spotify',
                                    'id': 'spotify',
                                    'type': 'user',
                                    'uri': 'spotify:user:spotify'},
                          'primary_color': None,
                          'public': None,
                          'snapshot_id': 'MTcwNzI0MzE2NiwwMDAwMDAwMDk1NmIzY2UxOTYwMjE1YTU3YjkyYjE3MTA3YWUwOGQ4',
                          'tracks': {'href': 'https://api.spotify.com/v1/playlists/37i9dQZF1DWTQwRw56TKNc/tracks',
                                     'total': 100},
                          'type': 'playlist',
                          'uri': 'spotify:playlist:37i9dQZF1DWTQwRw56TKNc'}],
               'limit': 1,
               'next': 'https://api.spotify.com/v1/search?query=low+key+warm+summer+day&type=playlist&offset=1&limit=1',
               'offset': 0,
               'previous': None,
               'total': 401}}

"""
