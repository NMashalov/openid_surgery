from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

from server.settings import OauthClientSettings
from server.handler import AuthHandler, StartHandler
from server.router import AuthRouter, StartRouter

app = FastAPI()

settings = OauthClientSettings()

app.include_router(
    AuthRouter(
        AuthHandler(settings=settings)
    )
)

app.include_router(
    StartRouter(
        StartHandler(settings=settings)
    )
)




