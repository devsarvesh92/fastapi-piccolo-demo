"""This module defines test environment settings."""

from pydantic_settings import BaseSettings


class ENVSETTINGS(BaseSettings):
    """Defines basic env vars for test environment."""

    # Database
    database_name: str | None = "testdb"
    database_host: str | None = "localhost"
    database_port: int | None = 5432
    database_user: str | None = "test"
    database_password: str | None = "P@ssw0rd"
    db_connection_pool_size: int | None = 10
