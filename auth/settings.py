from pydantic_settings import BaseSettings, SettingsConfigDict


class ClientSettings(BaseSettings):
    provider_url:str
    client_id: str
    client_secret: str

    model_config = SettingsConfigDict(env_file='.env')