import os
import requests
from classes import Weather


# Retrieves the OpenWeatherMap API key from the environment variables
def get_api_key():
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if api_key is None:
        print("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
    return api_key


# Takes latitude, longitude, and API key as parameters and constructs the query parameters
# for the OpenWeatherMap API request, then returns a dictionary containing the query parameters
def build_query_params(lat, lon, api_key):
    return {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }


# Takes the query parameters, sends a request to the OpenWeatherMap API,
# and retrieves the weather data, then returns the JSON response if successful
def fetch_weather_data(query_params):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        forecast_data = response.json()
        return forecast_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Takes the forecast data (JSON response) and extracts relevant information
# like wind speed, weather icon, conditions, and temperature, then returns
# a tuple containing windspeed, icon, conditions, and temp.
def parse_forecast_data(forecast_data):
    windspeed = float(forecast_data['wind']['speed'])
    icon = str(forecast_data['weather'][0]['icon'])
    conditions = str(forecast_data['weather'][0]['main'])
    temp = float(forecast_data['main']['temp'])
    return windspeed, icon, conditions, temp


# The main function that fetches the weather forecast using the OpenWeatherMap API,
# then returns a tuple with weather information (windspeed, icon, conditions, temp) if successful
def get_weather_forecast(lon, lat):
    api_key = get_api_key()
    if api_key:
        query_params = build_query_params(lat, lon, api_key)
        forecast_data = fetch_weather_data(query_params)
        if forecast_data:
            windspeed, icon, conditions, temp = parse_forecast_data(forecast_data)
            weather_object = Weather(windspeed, icon, conditions, temp)
            return weather_object
    return None
