import unittest
from tests.web.test_owm_http_client import TestOpenWeatherMapHttpClient
from tests.serialization.test_serialize_forecast import TestSerializeForecast


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOpenWeatherMapHttpClient())
    suite.addTest(TestSerializeForecast())

    unittest.main()
