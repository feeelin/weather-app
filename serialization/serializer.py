from pydantic import BaseModel, Field, field_validator
from serialization.serialize_coords import Coordinates
from serialization.serialize_forecast import Weather
from serialization.serialize_primary import Primary
from serialization.serialize_wind import Wind


# noinspection PyNestedDecorators
class GeneralForecast(BaseModel):
    coordinates: Coordinates = Field(alias='coordinates', validation_alias='coord')
    weather: Weather | list = Field(alias='weather')
    primary: Primary = Field(alias='primary', validation_alias='main')
    wind: Wind = Field(alias='wind')
    rain: dict | float = Field(alias='rain')
    clouds: dict | int = Field(alias='clouds')
    name: str = Field(alias='name')

    @field_validator('weather')
    @classmethod
    def validate_weather(cls, value):
        return Weather.model_validate(value[0])

    @field_validator('rain')
    @classmethod
    def validate_rain(cls, value):
        return value['1h']

    @field_validator('clouds')
    @classmethod
    def validate_clouds(cls, value):
        return value['all']

