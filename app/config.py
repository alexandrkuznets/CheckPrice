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
    rabbitmq_default_user: str
    rabbitmq_default_password: str
    cookie_wb: Dict[str, str]
    email_sender: str
    email_password: str
    email_port: int = 465
    email_server: str = "smtp.yandex.ru"
    email_host: str

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

