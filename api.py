from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def default():
    return {"msg": "Hello World"}