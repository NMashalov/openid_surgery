from pydantic_settings import BaseSettings, SettingsConfigDict


class OauthClientSettings(BaseSettings):
    provider_url:str
    server_port: int
    client_id: str
    client_secret: str

    model_config = SettingsConfigDict(env_file='.env',extra='ignore')