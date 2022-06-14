from api.routers.router import Router

class BookRouter(Router):
    
    def __init__(self) -> None:
        super().__init__()
        # self.prefix = "/book"

    def set_routes(self):
        @self.router.get("/", tags=["users"])
        async def get_book():
            return {"book-root": "This is the root / of boook"}

        return super().set_routes()
