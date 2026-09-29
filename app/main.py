from fastapi import FastAPI

app = FastAPI()

# Define a simple response model (optional, but keeps type hints clear)
class MessageResponse(BaseModel):
    message: str

@app.get("/", response_model=MessageResponse)
async def read_root():
    """Return a friendly greeting message when the app starts."""
    return {"message": "Hello, world!"}
