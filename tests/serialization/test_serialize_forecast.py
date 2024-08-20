import unittest
from serialization.serialize_forecast import Weather


class TestSerializeForecast(unittest.TestCase):
    def test_weather(self):
        test_obj = {
            "id": 501,
            "main": "Rain",
            "description": "moderate rain",
            "icon": "10d"
        }
        test_weather = Weather(id=501,main="Rain", description="moderate rain", icon="10d")
        test_weather_2 = Weather.model_validate(test_obj)

        self.assertEqual(test_weather == test_weather_2, True)

