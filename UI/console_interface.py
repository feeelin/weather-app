from web.OpenWeatherMapHttpClient import OpenWeatherMapHttpClient as OWM
from config import settings
from serialization.serializer import GeneralClass


class ConsoleInterface:
    def __init__(self):
        pass

    def hello_screen(self):
        pass

    def city_screen(self):
        pass

    def data_screen(self):
        pass

    def __process_data(self, city: str):
        self.web_client = OWM('https://api.openweathermap.org', settings.API_KEY)
        coords = self.web_client.get_city_coords(city)
        json_forecast = self.web_client.get_city_forecast(coords)

        result = GeneralClass()
        result.model_validate(json_forecast)

        return result

