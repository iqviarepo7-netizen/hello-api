from fastapi import FastAPI

app = FastAPI()

# Existing routes (if any) would be defined here

@app.get("/hello_world", response_model=dict)
def hello_world():
    """Return a simple greeting message."""
    return {"message": "Hello, world!"}
