from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

from client.settings import ClientSettings

class ImageClient:
    def __init__(self,settings: ClientSettings):
        self.settings = settings
        self.client = Client(
            client_id=self.settings.client_id,
            client_authn_method=CLIENT_AUTHN_METHOD    
        )

    def discover(self, uid: str):
        issuer = self.client.discover(uid)
        provider_configs = self.client.provider_config(issuer)
        return issuer, provider_configs
