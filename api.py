from datetime import datetime

import uvicorn
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
    # Process data from the Enviro Urban
    # https://github.com/pimoroni/enviro/blob/main/documentation/boards/enviro-urban.md
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)