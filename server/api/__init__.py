from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(docs_url='/', title='FallHack 2020 Api')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://asim-shrestha.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# from .database import db

# app.add_event_handler("startup", db.connect)
# app.add_event_handler("shutdown", db.disconnect)

from . import routes

from . import sockets
app.mount('/', sockets.sio_app)