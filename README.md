# WeatherMood: A vehicle for nostalgic experience

## General Project Info
Welcome to the WeatherMood App!

This application allows users to get weather information for a specific city and state and discover Spotify playlists based on their mood or theme.

WeatherMood works by taking into account the weather and place you're experiencing at a given moment and present you with a playlist of songs to listen to.

It stores the location, weather, playlist and time, so you can come back at any time to relive the experience. 

### Inspirations
Studies have shown that music and memory are strongly linked. We've all had an experience where we're transported through time when an old song comes on. Scientists behind the study referenced in this 2013 [article](https://www.psychologytoday.com/us/blog/the-athletes-way/201312/why-do-the-songs-your-past-evoke-such-vivid-memories) called the experience *‘music-evoked autobiographical memories’* (***MEAMs***).

#### Jon's Experience With MEAMs
There's certain songs I listened to back in the late 00s like ["The Man Who Can't Be Moved"](https://youtu.be/uAYUfGWD9SM?si=27fr-ycpJzW2-Xsl) and ["Big Yellow Taxi"]( https://youtu.be/tvtJPs8IDgU?si=zAF4BguImWDSWhHe) while reading mediocre books about vampires and werewolves that I immediately remember ridiculous details about. Not only those details, but the thoughts about life, school, and the relationships I was trying to cultivate at the time come back to me when I hear songs from that playlist. 

#### Emerlyn's Experience With MEAMs
As an individual deeply entrenched in the world of music, I've often found myself captivated by the profound connections between melodies and memories. You would see me with my headphones during my daily morning walk. Certain songs have the remarkable ability to transport me back to specific moments in my life. I usually get Last Song Syndrome (LSS) that shows the profound impact of music on memory. Even after the song has ended, the song replays in my mind durin the day, leaving an imprint on my consciousness. Just like Jon, I've listened to 'The Script', who are one of my favorite bands. When I listen to ["It's Time"](https://youtu.be/sENM2wA_FTg?si=WK5zxN6xbySxxqMf) by 'Imagine Dragons', I vividly remember my sister first introducing this song to me on a hot summer day as we listen in our apartment building both singing out loud. 

#### Riley's Experience With MEAMs

### A gentle warning 
The article linked above mentions that the longer it's been since you've heard a song, the more vivid the memories can be. Repeated listening can dampen the effects by repeatedly allowing those same neural circuits to be accessed and new information being associated. 

## Set-up
### Public APIs Used
1. OpenWeatherMap API for weather information
2. Spotify API for playlist discovery
3. Nominatim API for geocoding services

### API Keys
You'll want to set up your own dev accounts with [OpenWeather](https://openweathermap.org/api) and [Spotify's Web API](https://developer.spotify.com/documentation/web-api) to get access to their APIs. 

- Spotify's API requires a client_id and client_secret to be passed to receive an access token with each call. 
- OpenWeather will give a single API key you can use. 
- Nominatum does't require an API key

### Environment Variables
Save the information in Environment Variables as follows:

|The Key|Environment Variable Name|
|---|---|
|OpenWeather| OPENWEATHER_API_KEY|
|Spotify client_id|SPOTIFY_WEB_DEV_WEATHERMOOD_ID|
|Spotify client_secret|SPOTIFY_WEB_DEV_WEATHERMOOD_SECRET|

## Later Hopes
- Add option to also allow a user to write a note at the time of creation, further assisting in memory recall
- Moving the program to a flask webapp
