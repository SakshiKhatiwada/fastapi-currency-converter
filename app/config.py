from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    site_title: str
    site_version: str
    
    model_config = SettingsConfigDict(env_file=".env")
    

settings = Settings()