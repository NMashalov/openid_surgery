import httpx
from random import choice
import string

from auth.client import ImageClient
from auth.settings import ClientSettings

def rndstr(size=16):
    # Pick a random string of size `size` from the alphabet
    alphabet = string.ascii_letters + string.digits
    return "".join([choice(alphabet) for _ in range(size)])

def finger(settings: ClientSettings):
    return httpx.get(
        settings.provider_url + ".well-known/openid-configuration"
    ).json()

def authorization(authorization_endpoint: str, settings: ClientSettings):
    state = rndstr(size=16)
    authorization_url = "{authorization_endpoint}?client_id={client_id}&response_type=code&scope=openid&state={state}".format(
        client_id=settings.client_id,
        authorization_endpoint=authorization_endpoint,
        state=state,
    )



def plain_experiment():
    finger_settings = finger()
    print(finger_settings)
    token_endpoint = finger_settings['token_endpoint']
    authorization_endpoint = finger_settings['authorization_endpoint']



def prepare_client():
    return ImageClient(
        settings= ClientSettings()
    )

def discover_experiment(image_client: ImageClient):
    client = prepare_client()
    issuer, provider_configs =  image_client.discover('7901f723-6b5d-4692-9d43-d28459194d56')
    print(issuer, provider_configs)

def main():
    plain_experiment()
    
    
    

main()



