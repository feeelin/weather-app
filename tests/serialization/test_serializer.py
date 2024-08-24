from serialization.serializer import GeneralForecast
import unittest


class TestGeneralForecast(unittest.TestCase):

    def test_general_forecast(self):
        data = {'coord': {'lon': 37.6175, 'lat': 54.193},
                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'пасмурно', 'icon': '04d'}],
                'base': 'stations',
                'main': {'temp': 22.76, 'feels_like': 22.19, 'temp_min': 22.76, 'temp_max': 22.76, 'pressure': 1020,
                         'humidity': 42, 'sea_level': 1020, 'grnd_level': 996}, 'visibility': 10000,
                'wind': {'speed': 1.74, 'deg': 331, 'gust': 1.65}, 'clouds': {'all': 100}, 'dt': 1724495596,
                'sys': {'country': 'RU', 'sunrise': 1724466214, 'sunset': 1724517632}, 'timezone': 10800, 'id': 480562,
                'name': 'Тула', 'cod': 200}

        result = GeneralForecast.model_validate(data)
