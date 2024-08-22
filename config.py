from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    API_KEY: str = '2bf227af1c09c8b5df6dd03178818f27'


settings = Settings()
