from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    API_KEY: str = '193860b304f6e0731ed43ab5c80339a8'


settings = Settings()
