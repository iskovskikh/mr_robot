from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    api_token: SecretStr = Field(default="", alias="INVEST_TOKEN")
