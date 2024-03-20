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
I have listened to a lot of songs in my life when I hear a certain black eyed peas song I remember my old neighborhood friend playing Call Of Duty cramped in a basement with 5 others when I was in elementary school. Another is watching Katie Perry's music video in band class middle school. Lastly was playing video games on my school provided chromebook with my friend on the phone and listening to Two Steps From Hell. As young as I am its nice to hear these older songs and reminice about my past rexperiencing the memories and the emotions with it.

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

### Dependencies
Openning the project directory in your terminal and running the below command with install all the requirements.
`pip install -r requirements.txt`

## Later Hopes
- Add option to also allow a user to write a note at the time of creation, further assisting in memory recall
- Moving the program to a flask webapp

---

# Using the program
In your terminal you have the option to immediately create a new weathermood object. 
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/d41a5ab9-2e8a-430b-86ae-3887d8aff216)

Creating the weathermood starts with entering your current city, selecting an option if more than one city exists with the same name, and finally entering a mood. 
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/0555a424-a429-4053-9f15-ede2b16e715c)

Immediately upon creation, the program will open Spotify in either your browser or the Spotify desktop application if you have it installed. 
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/b21f5cad-932b-4c6a-b339-3d5bce954d42)

The application returns to the main menu, and you're able to look at weathermoods created in the past. 
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/0b9359da-4287-419a-91dd-28ba66af2b21)

Favorite options are toggleable, so you can look at only your favorites if you'd like. 
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/a0af6876-ae78-45c3-8d06-206dba3a394f)
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/7ca92bfd-16f3-4e8f-acc8-e50c6349b2cd)

Or look at all past created weathermoods.
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/54967c6f-6964-4d31-8035-f06c6f0b0a6d)

You can open the playlist again, toggle the favorite status, or delete the weathermood whether you open it from Favorites or All
![image](https://github.com/Jon-117/project3_weathermoodmusic/assets/38222965/3036cc0c-a151-4839-8106-2aeba5acab9c)

Unfortunately, current limitations with the console-menu package require us to fully back out of a menu (or submenu) and then re-enter it to see changes made. This means that after interacting with a weathermood you'll have to fully back out of the menu which displays them to see changes. We were unable to create a function to refresh a menu when moving backwards through the menus. It may be possible with another package such as curses, but we weren't able to pivot quick enough to implement this. 

