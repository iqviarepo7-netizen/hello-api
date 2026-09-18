from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_world")
def hello_world():
    return {"message": "Hello, world!"}


@app.get("/hello_hi", response_model=dict)
def hello_hi():
    return {"message": "Hello, hi!"}
