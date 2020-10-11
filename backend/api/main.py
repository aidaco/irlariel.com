# Aidan Courtney 2020, see incl. license for details.

from fastapi import FastAPI

from fastapi_config import Config
from fastapi_auth import Authentication

from .routers import users, products

def create_app():
    app = FastAPI()
    app.middleware('http')(Config('config.Config'))
    app.middleware('http')(Authentication())
    app.include_router(users.router, prefix='/users')
    app.include_router(products.router, prefix="/products")
    return app