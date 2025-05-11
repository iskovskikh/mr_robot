from enum import StrEnum, auto

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field
class ApiTargetEnum(StrEnum):
    PUBLIC = auto()
    SANDBOX = auto()

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    api_token: SecretStr = Field(default="", alias="INVEST_TOKEN")
    api_target: ApiTargetEnum = Field(default=ApiTargetEnum.SANDBOX)
