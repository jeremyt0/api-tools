from fastapi import FastAPI
import uvicorn

from api.controllers.routercontroller import RouterController

class API:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(API, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.app = FastAPI()
        self.routers = RouterController()
        
        self.host = "0.0.0.0"
        self.port = 8080

        self.add_routes_default()
        self.add_routers()
        
    def add_routers(self):
        self.routers.add_to_app(self.app)

    def add_routes_default(self):
        @self.app.get("/")
        def read_root():
            return {"hello": "Message here is really cool!"}

        @self.app.get("/info")
        async def read_info():
            return {"info": "This is my fastapi 0.0.1"}


    def run(self):
        # Run Server code here
        uvicorn.run(self.app, host=self.host, port=self.port, reload=False)


