from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world")
async def read_hello_world():
    return {"message": "Hello World!"}

@app.get("/hello_hi")
async def read_hello_hi():
    return {"message": "Hi there!"}
