# app/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str = "brtiot"
    ORIGINS: list = ["http://localhost:3000"]
    API_PORT: int = 8080

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
