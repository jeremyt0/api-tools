from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Helloo": "World"}

@app.get("/info")
async def read_info():
    return {"info": "This is my fastapi 0.0.1"}


# Run in cmd: uvicorn example:app --reload

if __name__=="__main__":
    # Run in python
    uvicorn.run("example:app", host="127.0.0.1", port=8000, log_level="info")
