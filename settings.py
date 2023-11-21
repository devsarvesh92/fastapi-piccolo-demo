"""This module defines test environment settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Defines basic env vars for test environment."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Database
    database_name: str
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    db_connection_pool_size: int = 10


ENVSETTINGS = Settings()
