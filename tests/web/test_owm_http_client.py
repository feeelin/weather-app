import unittest
from web.OpenWeatherMapHttpClient import OpenWeatherMapHttpClient
from config import settings


class TestOpenWeatherMapHttpClient(unittest.TestCase):
    def setUp(self):
        self.client = OpenWeatherMapHttpClient('https://api.openweathermap.org', settings.API_KEY)

    def test_city_response(self):
        result = self.client.get_city_coords('Tula')
        self.assertEqual(type(result), dict)

    def test_forecast_response(self):
        result = self.client.get_city_forecast([{"lat": 15, "lon": 15}])
        self.assertEqual(type(result), dict)
