import unittest
from serialize_wind import Wind


class TestWind(unittest.TestCase):
    def test_wind(self):
        test_obj = {
            "speed": 0.62,
            "deg": 349,
            "gust": 1.18
        }
        test_wind = Wind(speed=0.62, deg=349, gust=1.18)
        test_wind_2 = Wind.model_validate(test_obj)
        self.assertEqual(test_wind == test_wind_2, True)


if __name__ == '__main__':
    unittest()
