from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = Field(default="NeuroRelatorio Pro", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    database_url: str = Field(
        default="postgresql+psycopg://neuro:neuro@localhost:5432/neurorelatorio",
        alias="DATABASE_URL",
    )
    jwt_secret: str = Field(default="change-me", alias="JWT_SECRET")
    ai_review_required: bool = Field(default=True, alias="AI_REVIEW_REQUIRED")


@lru_cache
def get_settings() -> Settings:
    return Settings()
