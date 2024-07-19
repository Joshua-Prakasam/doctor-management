"""Global config for app."""

from pathlib import Path

from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["app_config"]


class Settings(BaseSettings):
    """Global Settings."""

    pg_dsn: PostgresDsn
    secret_key: SecretStr

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent.parent
        / "server.env",
    )


# mypy: disable-error-code="call-arg"
app_config = Settings()
