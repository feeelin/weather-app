from pydantic import BaseModel


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float
