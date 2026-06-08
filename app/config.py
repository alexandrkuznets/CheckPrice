from typing import Dict
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_port: int
    postgres_host: str
    postgres_db: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    rabbitmq_pass: str
    cookie_wb: Dict[str, str]

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

