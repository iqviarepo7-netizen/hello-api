from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello_world_i_am_mk")
def hello_world_i_am_mk():
    return {"message": "Hello, world! I am mk"}
