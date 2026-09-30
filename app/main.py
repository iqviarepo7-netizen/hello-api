from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world_i_am_mk")
def hello_world():
    return {"message": "Hello, world! I am mk"}

@app.get("/hello_vanakam")
def hello_vanakam():
    return {"message": "Hello, vanakam!"}
