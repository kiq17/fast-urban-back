from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    acess_token_expire_minutes: int
    dbprod_url: str

    class Config:
        env_file = ".env"


settings = Settings()