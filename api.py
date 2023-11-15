from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Reading(BaseModel):
    nickname: str
    model: str
    uid: str
    timestamp: datetime

@app.post("/")
def default(reading: Reading):
    return {"msg": "Hello World"}