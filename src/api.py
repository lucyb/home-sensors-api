import uvicorn
from fastapi import FastAPI

from . import database
from .models import Urban

app = FastAPI()

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