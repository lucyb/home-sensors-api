from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Reading(BaseModel):
    nickname: str

@app.post("/")
def default(reading: Reading):
    return {"msg": "Hello World"}