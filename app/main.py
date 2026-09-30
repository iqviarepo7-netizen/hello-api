from fastapi import FastAPI

app = FastAPI()

# Existing routes (if any) would be defined above or below this comment

@app.get("/hello_world_i_am_mk")
def hello_world_i_am_mk():
    """Return a simple greeting JSON payload.

    This endpoint is added to satisfy SCRUM-7.
    """
    return {"message": "Hello, world! I am mk"}
