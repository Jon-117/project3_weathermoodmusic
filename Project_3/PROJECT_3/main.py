import os
import geoCoding
import spotifyapi






if __name__ == "__main__":
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    if api_key is None:
        print("API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    else:
        city = input("Enter the city for the weather forecast: ")
        lon,lat = geoCoding.geo_coding(city)
        weather = getWeatherForecast.get_weather_forecast(api_key,lon,lat)
        spotifyapi.printPlaylist(weather)