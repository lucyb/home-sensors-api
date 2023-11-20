from datetime import datetime

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import database

app = FastAPI()

class Reading(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    noise: float
    pm1: float
    pm2_5: float
    pm10: float
    voltage: float

class Urban(BaseModel):
    nickname: str
    model: str
    uid: str
    timestamp: datetime
    readings: Reading

@app.get("/")
def default():
    return

@app.post("/urban")
def urban(urban: Urban):
    # Process data from the Enviro Urban
    # https://github.com/pimoroni/enviro/blob/main/documentation/boards/enviro-urban.md
    return database.write(urban)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)