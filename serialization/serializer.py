from pydantic import BaseModel, Field
import json
from typing import List
# ******************************
from serialize_forecast import Weather
from serialize_wind import Wind


# def read_input_json(filename: str) -> dict:
#     with open(file=filename, encoding="UTF-8") as file:
#         output = json.load(file)
#     return output


class Rain(BaseModel):
    oneH: float = Field(alias='oneH', validation_alias='1h')

class Clouds(BaseModel):
    all: int


class Serialize(BaseModel):
    weather: List[Weather]
    wind: Wind
    visibility: int
    rain: Rain
    clouds: Clouds



# if __name__ == "__main__":
#     example_data = read_input_json('data.json')
#     test = Serialize(**example_data)
#     print(test)
#==============================================================================================================
# Импортируем стандарную бибилиотеку для работы с JSON
import json

# Импортируем необходимые для моего кривого синтаксиса бибилиотеки
from numbers import Real
from pydoc import visiblename

# from __future__ import ty... - Если не будет работать Pydantic

# импортируем модуль из бибилиотеки Pydantic
from pydantic import BaseModel

# Импортируем обработанные объекты и переменные из программ (парсинга) коллег
from .serialize_main import *
from .serialize_coords import *
from .serialize_forecast import *
from .serialize_wind import *

# Warcraft III - "Нужно больше..." бибилиотек


# Основной большой класс, который бы хотел Валерий, но его написал Григорий, поэтому: "Валерий прости..."
class GeneralClass(BaseModel):
  pass
  # Видимость (метры)
  visibility: int 

  # Класс "дождь" со свойством "объем осадков за последний час"
  class Rain(BaseModel):
    _1h: float
  
  # Класс "облака" со свойством "облачность" (%)"
  class Clouds(BaseModel):
    _all: int
  

class Sys(BaseModel): 
    country: str
    # время расвета (конвертировать тип данных)
    sunrise: int
    # время заката  (конвертировать тип данных)
    sunset: int

# Исходный JSON
""" 
#  Объект из serialize_coords.py
--------------------------------
{
  "coord": {
    "lon": 10.99,  // Долгота
    "lat": 44.34   // Широта
  },
--------------------------------
#  Объект из serialize_forecast.py
--------------------------------
  "weather": [
    {
      "id": 501,
      "main": "Rain",           -          Группа погодных параметров (дождь, снег, облачность и т.д.)
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
--------------------------------
  # Внутренний параметр (рудимент - не используется)
--------------------------------
  "base": "stations",
--------------------------------
#  Объект из serialize_main.py
--------------------------------
  "main": {
    "temp": 298.48,             -          Температура, K (перевести в Цельсия)
    "feels_like": 298.74,       -          Температура с учетом воприятия человеком, K (перевести в Цельсия)
    "temp_min": 297.56,         -          Минимальная температура, K (перевести в Цельсия)
    "temp_max": 300.05,         -          Максимальная температура, K (перевести в Цельсия)
    "pressure": 1015,           -          Атмосферное давление на уровне моря, ГПа
    "humidity": 64,             -          Влажность, %
    "sea_level": 1015,          -          Атмосферное давление на уровне моря, ГПа
    "grnd_level": 933           -          Атмосферное давление на уровне земли, ГПа
  },
--------------------------------
    # Видимость и ветер (нужна)
--------------------------------
  "visibility": 10000  // видимость в метрах
--------------------------------
  #  Объект из serialize_wind.py
--------------------------------
  "wind": {
    "speed": 0.62,  // скорость ветра в м/с
    "deg": 349,     // направление ветра в градусах
    "gust": 1.18    // максимальные порывы ветра в м/с
  },
--------------------------------
    # Объем осадков за последний час (нужно)
--------------------------------
  "rain": {
    "1h": 3.16  // Объем осадков за последний час
  },
--------------------------------
    # Облачность (нужна)
--------------------------------
  "clouds": {
    "all": 100  // облачность в %
  },
--------------------------------
    # Нужно частично
--------------------------------
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",        //  Код страны
    "sunrise": 1661834187, // Время восхода солнца
    "sunset": 1661882248   // Время заката
  },
--------------------------------
    # Город (нужно)
--------------------------------
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",        // Наименование города
  "cod": 200
}                   
"""
