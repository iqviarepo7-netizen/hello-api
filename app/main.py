from fastapi import FastAPI

app = FastAPI()

# Existing routes and logic may be here

@app.get("/hello_world_i_am_mk")
async def hello_world_i_am_mk():
    """Return a JSON greeting message."""
    return {"message": "Hello, world! I am mk"}
