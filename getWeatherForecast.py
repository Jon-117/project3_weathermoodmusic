"""This code provides a simple interface to fetch weather forecast data and store
it in an instance of the Weather class. The user can then access the weather information
from the instance variables."""

import requests


class Weather:
    # method initializes the instance variables to None,
    # so that the values for these attributes will be set later based on actual weather data
    def __init__(self) -> None:
        self.windspeed = None
        self.icon = None
        self.conditions = None
        self.temp = None

    # method takes three parameters to fetch the weather forecast from the OpenWeatherMap API
    # uses the provided latitude and longitude to create a query for the API request
    def get_weather_forecast(self, api_key, lon, lat):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"

        query_params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key  # You can change this to 'imperial' for Fahrenheit
        }
        try:
            response = requests.get(base_url, params=query_params)
            # checks if the response contains any HTTP error status codes
            # and raises an exception if an error is detected
            response.raise_for_status()
            # method parses the JSON response to extract relevant weather information
            # such as wind speed, weather icon, conditions, and temperature
            forecast_data = response.json()
            self.windspeed = forecast_data['wind']['speed']
            self.icon = forecast_data['weather'][0]['icon']
            self.conditions = forecast_data['weather'][0]['main']
            self.temp = forecast_data['main']['temp']
        except Exception as e:
            # printing detail of exception here
            print(f"An unexpected error occurred: {e}")
