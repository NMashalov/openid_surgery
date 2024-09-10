from fastapi import FastAPI
import httpx
from auth.settings import ClientSettings



app = FastAPI()

@app.get()
def auth(session_state: str, state: str, code: str):
    settings = ClientSettings()
    resp = httpx.post(
        token_endpoint,
        data={
            "client_id": settings.client_id,
            "client_secret": settings.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.OIDC_REDIRECT_URIS[0],
        },
    )
