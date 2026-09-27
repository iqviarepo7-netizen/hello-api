from fastapi import FastAPI

app = FastAPI()

# Existing routes would be defined above or below this comment.

@app.get("/hello_world")
async def hello_world() -> dict:
    """Return a simple greeting message as JSON."""
    return {"message": "Hello, World!"}
