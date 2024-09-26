from fastapi import APIRouter
from server.handler import AuthHandler, StartHandler

class StartRouter(APIRouter):
    def __init__(self,handler: StartHandler):
        super().__init__(tags=['Auth'])
        self.add_api_route(
            path ='/',
            endpoint=handler.start_no_auth,
            methods=['GET']

        ) 
        self.add_api_route(
            path ='/start',
            endpoint=handler.start_auth,
            methods=['GET']
        ) 


class AuthRouter(APIRouter):
    def __init__(self,handler: AuthHandler):
        super().__init__(tags=['Auth'])
        self.add_api_route(
            path ='/callback',
            endpoint=handler.callback,
            methods=['GET'] 
        ) 


auth_router = APIRouter(tags=['Auth'])

