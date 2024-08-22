import unittest
from serialization.serialize_wind import Wind


class TestSerializeWind(unittest.TestCase):
    def test_wind(self):
        test_obj_wind = {
            "speed": 0.62,
            "deg": 349,
            "gust": 1.18
        }
        test_wind = Wind(speed=0.62, deg=349, gust=1.18)
        test_wind_2 = Wind.model_validate(test_obj_wind)
        self.assertEqual(test_wind == test_wind_2, True)
