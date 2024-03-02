import os
import requests


def get_weather_forecast(lon, lat):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    api_key = os.getenv("OPENWEATHER_API_KEY")  # Get API key from environment variable

    if api_key is None:
        print("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
        return None

    query_params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        forecast_data = response.json()

        windspeed = forecast_data['wind']['speed']
        icon = forecast_data['weather'][0]['icon']
        conditions = forecast_data['weather'][0]['main']
        temp = forecast_data['main']['temp']

        return windspeed, icon, conditions, temp

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None