import unittest
from tests.web.test_owm_http_client import TestOpenWeatherMapHttpClient
from tests.serialization.test_serialize_forecast import TestSerializeForecast
from tests.serialization.test_serialize_wind import TestSerializeWind
from tests.serialization.test_serialize_primary import TestSerializePrimary
from tests.serialization.test_serializer import TestGeneralForecast


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOpenWeatherMapHttpClient())
    suite.addTest(TestSerializeForecast())
    suite.addTest(TestSerializeWind())
    suite.addTest(TestSerializePrimary())
    suite.addTest(TestGeneralForecast())
    unittest.main()
