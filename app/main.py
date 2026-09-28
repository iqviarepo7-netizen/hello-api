from fastapi import FastAPI

app = FastAPI()

# Existing routes...

@app.get("/hello_world_i_am_mk")
async def hello_world_i_am_mk():
    return {"message": "Hello, world! I am mk"}
