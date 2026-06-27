from typing import Dict
from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: SecretStr
    postgres_port: int
    postgres_host: str
    postgres_db: str
    secret_key: SecretStr
    algorithm: str
    access_token_expire_minutes: int
    rabbitmq_default_user: str
    rabbitmq_default_pass: SecretStr
    cookie_wb: Dict[str, str]
    email_sender: str
    email_password: SecretStr
    email_host: str
    email_port: int = 465
    email_server: str = "smtp.yandex.ru"


    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

