from fastapi import FastAPI

app = FastAPI()

# Existing routes (if any) would be defined above or imported here

@app.get("/hello_world_i_am_mk")
def hello_world_i_am_mk():
    """Return a simple greeting JSON.

    This endpoint is added for SCRUM-7.
    """
    return {"message": "Hello, world! I am MK"}
