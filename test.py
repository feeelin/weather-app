import unittest
from tests.web.test_owm_http_client import TestOpenWeatherMapHttpClient

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOpenWeatherMapHttpClient())

    unittest.main()
