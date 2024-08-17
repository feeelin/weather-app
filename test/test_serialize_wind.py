import unittest
from serialize_wind import Wind, read_input_json


class TestMain(unittest.TestCase):
    def test_wind(self):
        example_data = read_input_json('data.json')
        wind = Wind(**example_data)
        self.assertEqual(type(wind.get_wind()), dict)


if __name__ == '__main__':
    unittest()
