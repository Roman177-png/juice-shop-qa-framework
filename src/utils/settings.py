from functools import lru_cache

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    base_url: HttpUrl = HttpUrl("http://localhost:3000")
    admin_email: str = "admin@juice-sh.op"
    admin_password: str = "admin123"


@lru_cache
def get_settings() -> Settings:
    return Settings()
