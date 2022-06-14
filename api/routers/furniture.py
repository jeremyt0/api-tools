from api.routers.router import Router

class FurnitureRouter(Router):
    
    def __init__(self) -> None:
        super().__init__()
        # self.prefix = "/furniture"

    def set_routes(self):
        @self.router.get("/", tags=["chairs"])
        async def get_test():
            return {"furniture-root": "This is the root / of furniture"}

        @self.router.get("/tables/", tags=["cool"])
        async def read_tables():
            return [{"name": "Cool table 1"}, {"name": "Cool table 2"}]

        return super().set_routes()

