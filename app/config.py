from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_port: int
    postgres_host: str
    postgres_db: str

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

