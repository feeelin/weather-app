import unittest

from serialize_primary import Primary


class TestSerializePrimary(unittest.TestCase):
    def test_primary(self):
        test_obj = {
            "temp": 298.48,
            "feels_like": 298.74,
            "temp_min": 297.56,
            "temp_max": 300.05,
            "pressure": 1015,
            "humidity": 64,
            "sea_level": 1015,
            "grnd_level": 933
        }
        test_primary = Primary(temp=298.48, feels_like=298.74, temp_min=297.56, temp_max=300.05, pressure=1015, humidity=64, sea_level=1015, grnd_level=933)
        test_primary2 = Primary.model_validate(test_obj)

        self.assertEqual(test_primary == test_primary2, True)
