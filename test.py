import unittest
from tests.web.test_owm_http_client import TestOpenWeatherMapHttpClient
from tests.serialization.test_serialize_forecast import TestSerializeForecast
from tests.serialization_wind.test_serialize_wind import TestWind


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOpenWeatherMapHttpClient())
    suite.addTest(TestSerializeForecast())
    suite.addTest(TestWind())
    unittest.main()
