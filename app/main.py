from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world")
async def hello_world():
    return {"message": "Hello, World!"}

# New endpoint as per SCRUM-7
@app.get("/hello_world_i_am_mk")
async def hello_world_i_am_mk():
    return {"message": "Hello, World! I am MK"}
