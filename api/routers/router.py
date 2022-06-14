from abc import ABC, abstractmethod

from fastapi import APIRouter

class Router(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Router, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.router = APIRouter()
        self.prefix = "/" + self.__module__.split(".")[-1]

        self.set_routes()

    @abstractmethod
    def set_routes(self):
        """Set all routes in here"""
        print(f"Setting {type(self).__name__} routes.")
        pass

