from typing import TypeAlias
from pydantic import BaseModel

Celsius: TypeAlias = float


class Primary(BaseModel):
    temp: Celsius
    feels_like: Celsius
    temp_min: Celsius
    temp_max: Celsius
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


