from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_fallback")
async def hello_fallback():
    """Return a simple JSON greeting message."""
    return {"message": "Hello, world!"}
