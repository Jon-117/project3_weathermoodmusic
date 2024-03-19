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