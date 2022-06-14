# import uvicorn
from api.controllers.api import API

api = API()
app = api.app

# Run in cmd: uvicorn main:app --reload --reload-delay 1.5

# if __name__=="__main__":
#     uvicorn.run("main:app", host=api.host, port=api.port, reload=True)
