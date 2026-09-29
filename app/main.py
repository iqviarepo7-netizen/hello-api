from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world_i_am_mk")
async def hello_world_i_am_mk():
    """Return a simple greeting message."""
    return {"message": "Hello, world! I'm mk"}
