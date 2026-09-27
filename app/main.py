from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world", response_model=dict)
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/hello_vanakam", response_model=dict)
def hello_vanakam():
    return {"message": "Vanakam!"}
