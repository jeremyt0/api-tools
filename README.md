# api-tools
First look at FastAPI.

Setting up an API respository with tools that can be reused.

# Setup

## Create a virtual environment for Python

I use venv

    python -m venv venv

## Activate virtual environment

Mac:
    
    source venv/bin/activate

Windows:
    
    TBC

## Install requirements

    pip install -r requirements.txt

# Quickstart

## Command line

Run the FastAPI `app` in `example.py`.

    uvicorn example:app --reload

## Python

Check your python version and run `example.py` with python command.

    python example.py

# Running

Example of server running.

    INFO:     Started server process [1234]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Enter route `http://127.0.0.1:8000` in browser url.

You should see `{"Helloo":"World"}` as the response.


# References

### FastAPI

Link [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

GitHub [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)

### Uvicorn

Link [https://www.uvicorn.org/](https://www.uvicorn.org/)

# Author

2022 Jeremy Tang

[GitHub](https://github.com/jeremyt0)
[LinkedIn](https://uk.linkedin.com/in/jeremytang0)

