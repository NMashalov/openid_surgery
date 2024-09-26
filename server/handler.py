from fastapi.responses import RedirectResponse, JSONResponse
from server.util import rndstr
from yarl import URL
import httpx

from server.settings import OauthClientSettings

class StartHandler:
    def __init__(self,settings: OauthClientSettings):

        self.callback_url = URL.build(scheme='http',host='localhost',port=5000,path='/callback')
        self.auth_url = URL.build(scheme='http',host='localhost',port=8080,path='/realms/master/protocol/openid-connect/auth')


    def identity(self, access_token: str):
        identity =httpx.get(
        f'http://localhost:8080/realms/master/protocol/openid-connect/userinfo',
        headers={"Authorization": f"Bearer {access_token}"},
        )

    def start_no_auth(self):        
        return RedirectResponse(
            url = str(self.auth_url.with_query(
                {
                    'client_id': 'image-client',
                    'response_type':'code',
                    'scope': 'openid',
                    'redirect_uri': str(self.callback_url),
                    'state': rndstr()
                }))
        )
    
    def start_auth(self):
        return 'hello'

    
class AuthHandler:
    def __init__(self, settings: OauthClientSettings):
        self.settings = settings
        self.token_url = URL.build(scheme='http',host='localhost',port=8080,path='/realms/master/protocol/openid-connect/token')
        self.start_page = URL.build(scheme='http',host='localhost',port=5000,path='/start')
        self.callback_url = URL.build(scheme='http',host='localhost',port=5000,path='/callback')

    def callback(self, code: str):
        resp =  httpx.post(
            str(self.token_url),
            data={
                "client_id": self.settings.client_id,
                "client_secret": self.settings.client_secret,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": str(self.callback_url)
            },
        )
        r = resp.json()
        response = RedirectResponse(url=str(self.start_page))
        response.set_cookie('access_token',r['access_token'])
        response.set_cookie('refresh_token',r['refresh_token'])
        return response

