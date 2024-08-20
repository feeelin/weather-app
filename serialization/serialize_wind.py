from pydantic import BaseModel


class Wind(BaseModel):
    speed: float or int
    deg: float or int
    gust: float or int
