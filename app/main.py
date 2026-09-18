from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world_i_am_mk", response_model=dict)
async def hello_world_i_am_mk():
    return {"message": "Hello, world! I am mk"}
