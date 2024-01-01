from datetime import datetime

from pydantic import BaseModel


class Reading(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    noise: float
    pm1: float
    pm2_5: float
    pm10: float


class Urban(BaseModel):
    nickname: str
    timestamp: datetime
    readings: Reading
