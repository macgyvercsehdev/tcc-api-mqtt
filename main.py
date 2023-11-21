from fastapi.middleware.cors import CORSMiddleware
from models.dao.mongo import client
import paho.mqtt.client as mqtt
from controller import router
from fastapi import FastAPI
from decouple import config

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)



