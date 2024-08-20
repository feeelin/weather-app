
class ConsoleInterface:
    def __init__(self):
        pass

    def __hello_screen(self):
        pass

    def __city_screen(self):
        pass

    def __data_screen(self, name_town):
        if name_town:
            self.name_town = name_town
        return name_town



    def __process_data(self, name_town: str):
        self.web_client = OWM('https://api.openweathermap.org', settings.API_KEY)
        coords = self.web_client.get_city_coords(name_town)
        json_forecast = self.web_client.get_city_forecast(coords)

        result = GeneralClass()
        result.model_validate(json_forecast)

        return result
