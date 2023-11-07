from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default():
    return {"msg": "Hello World"}