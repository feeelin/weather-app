from UI.console_interface import ConsoleInterface
from web.OpenWeatherMapHttpClient import OpenWeatherMapHttpClient as OWM
from serialization.serializer import GeneralForecast
from config import settings
import sys


class Program:
    def __init__(self):
        self.interface = ConsoleInterface()
        print(self.interface.hello_screen())
        self.read_user_input()

    def read_user_input(self) -> None:
        option = input(self.interface.menu_screen())

        if self.interface.check_option(option):
            self.__run_option(int(option))
        else:
            self.read_user_input()

    def __run_option(self, option: int) -> None:
        if option == 1:
            self.__get_forecast()
        else:
            print(self.interface.goodbye)
            sys.exit()

    def __get_forecast(self) -> None:
        city = input(self.interface.city_screen())
        print(self.__process_data(city))

    def __process_data(self, city: str):
        self.web_client = OWM('https://api.openweathermap.org', settings.API_KEY)
        coords = self.web_client.get_city_coords(city)
        json_forecast = self.web_client.get_city_forecast(coords)

        print(json_forecast)
        result = GeneralForecast.model_validate(json_forecast)

        return result


if __name__ == "__main__":
    Program()
