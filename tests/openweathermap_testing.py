import unittest
import sys
sys.path.append("..")
from unittest.mock import patch
from getWeatherForecast import get_weather_forecast


class TestWeatherAPI(unittest.TestCase):
    @patch('getWeatherForecast.requests.get')
    def test_get_weather_data(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {
            'base': 'stations',
            'clouds': {'all': 20},
            'cod': 200,
            'coord': {'lat': 44.98, 'lon': -93.2638},
            'dt': 1708306701,
            'id': 5037649,
            'main': {'feels_like': 19.44,
                     'humidity': 72,
                     'pressure': 1015,
                     'temp': 28.18,
                     'temp_max': 30.87,
                     'temp_min': 24.39},
            'name': 'Minneapolis',
            'sys': {'country': 'US',
                    'id': 2012563,
                    'sunrise': 1708261812,
                    'sunset': 1708299847,
                    'type': 2},
            'timezone': -21600,
            'visibility': 10000,
            'weather': [{'description': 'few clouds',
                         'icon': '02n',
                         'id': 801,
                         'main': 'Clouds'}],
            'wind': {'deg': 230, 'speed': 9.22}
        }

        # Set up the mock for requests.get
        mock_get.return_value = mock_response

        # Call the function that makes the API request
        result = get_weather_forecast(44.98,-93.2638)
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result.icon, mock_response.json()['weather'][0]['icon'])
        self.assertEqual(result.temp, mock_response.json()['main']['temp'])
        self.assertEqual(result.windspeed, mock_response.json()['wind']['speed'])
        self.assertEqual(result.conditions, mock_response.json()['weather'][0]['main'])


if __name__ == '__main__':
    unittest.main()
