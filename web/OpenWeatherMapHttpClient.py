from web.HttpClient import HttpClient
from config import settings
import requests


class OpenWeatherMapHttpClient(HttpClient):

    def get_city_coords(self, city) -> dict:
        with requests.get(f'{self._session.base_url}/geo/1.0/direct', params={'q': city, 'appid': settings.API_KEY}) as response:
            return response.json()

    def get_city_forecast(self, city) -> dict:
        with requests.get(url=f'{self._session.base_url}/data/2.5/weather',
                          params={'lat': city[0]['lat'],
                                  'lon': city[0]['lon'],
                                  'appid': settings.API_KEY,
                                  'lang': 'ru',
                                  'units': 'metric'
                                  }
                          ) as response:
            return response.json()
