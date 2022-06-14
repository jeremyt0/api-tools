from api.routers.book import BookRouter
from api.routers.furniture import FurnitureRouter


class RouterController:
    """Routers class which is a controller for all routers.
    """

    def __init__(self) -> None:
        self.routers = []
        
        self.add_routers()

    def add_to_app(self, app):
        """Function to add routers to main API app."""
        for router in self.routers:
            app.include_router(router.router, prefix=router.prefix)

    def add_routers(self):
        # TODO: Find all routers in routers dir and add to controller
        self.routers.append(BookRouter())
        self.routers.append(FurnitureRouter())
        pass
    
