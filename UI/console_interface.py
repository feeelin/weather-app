from web.OpenWeatherMapHttpClient import OpenWeatherMapHttpClient as OWM
from config import settings
from serialization.serializer import GeneralForecast


class ConsoleInterface:
    def __init__(self):
        self.option_error = 'Введена неверная опция!'
        self.goodbye = "До встречи!"
        self.options = [0, 1]

        self.__greeting = 'Привет!\nДобро пожаловать в weather-app!\n\n'
        self.__menu_options = 'Меню:\n[1] - Получить прогноз на сегодня\n[0] - Закрыть приложение\n\n'
        self.__city_input = 'Введите название города: '

    def hello_screen(self):
        return self.__greeting

    def menu_screen(self):
        return self.__menu_options

    def city_screen(self):
        return self.__city_input

    def data_screen(self, name_town: str):
        if name_town:
            self.name_town = name_town
        return name_town

    def check_option(self, option: str) -> bool:
        try:
            option = int(option)
            if option in self.options:
                return True
            return False
        except ValueError:
            return False



