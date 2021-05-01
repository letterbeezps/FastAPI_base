from fastapi import FastAPI
from app.routers import baseRouter

from fastapi import Request

from app.models import Base
from app.models import engin

# init db
Base.metadata.create_all(engin)

import time

def add_middleware(app: FastAPI):
    @app.middleware("http")
    async def mid_base(request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        end = time.time()
        response.headers['X-Process-Time'] = str(end-start)
        return response

def add_route(app: FastAPI):
    app.include_router(baseRouter)

def create_app():
    app = FastAPI()

    add_middleware(app)
    
    add_route(app)

    return app
