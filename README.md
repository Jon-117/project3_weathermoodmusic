# Weathermood: A vehicle for nostalgic experience


## General Project Info
Weathermood works by taking into account the weather and place you're experiencing at a given moment and present you with a playlist of songs to listen to. 

It stores the location, weather, playlist and time so you can come back at any time to relive the experience. 

### Inspirations
Studies have shown that music and memory are strongly linked. We've all had an experience where we're transported through time when an old song comes on. Scientists behind the study referenced in this 2013 [article](https://www.psychologytoday.com/us/blog/the-athletes-way/201312/why-do-the-songs-your-past-evoke-such-vivid-memories) called the experience *‘music-evoked autobiographical memories’* (***MEAMs***) 

#### Jon's Experience With MEAMs
There's certain songs I listened to back in the late 00s like ["The Man Who Can't Be Moved"](https://youtu.be/uAYUfGWD9SM?si=27fr-ycpJzW2-Xsl) and ["Big Yellow Taxi"](https://youtu.be/tvtJPs8IDgU?si=zAF4BguImWDSWhHe) while reading mediocre books about vampires and werewolves that I immediately remember ridiculous details about. Not only those details, but the thoughts about life, school, and the relationships I was trying to cultivate at the time come back to me when I hear songs from that playlist. 

#### Emerlyn's Experience With MEAMs


#### Riley's Experience With MEAMs


### A gentle warning 
The article linked above mentions that the longer it's been since you've heard a song, the more vivid the memories can be. Repeated listening can dampen the effects by repeatedly allowing those same neural circuits to be accessed and new information being associated. 

## Set-up
### API Keys & Environment Variables
You'll want to set up your own dev accounts with [OpenWeather](https://openweathermap.org/api) and [Spotify's Web API](https://developer.spotify.com/documentation/web-api) to get access to their APIs. 

- Spotify's API requires a client_id and client_secret to be passed to receive an access token with each call. 
- OpenWeather will give a single API key you can use. 
- Nominatum does't require an API key

Save the information in Environment Variables as follows:

|The Key|Environment Variable Name|
|---|---|
|OpenWeather| OPENWEATHER_API_KEY|
|Spotify client_id|SPOTIFY_WEB_DEV_WEATHERMOOD_ID|
|Spotify client_secret|SPOTIFY_WEB_DEV_WEATHERMOOD_SECRET|

## Later Hopes
- Add option to also allow a user to write a note at the time of creation, further assisting in memory recall
- Moving the program to a flask webapp
