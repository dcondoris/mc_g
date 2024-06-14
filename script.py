from fastapi import FastAPI

app = FastAPI()


@app.get("/addition")
def addition(x: int, y: int):
    return x + y


@app.get("/soustraction")
def soustraction(x: int, y: int):
    return x - y
