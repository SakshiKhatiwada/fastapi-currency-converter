from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    site_title: str
    site_version: str
    api_key: str
    env: str = "LOCAL"

    model_config = SettingsConfigDict(
        env_file=".env" if Path(".env").exists() else ".env.example"
    )


settings = Settings()
