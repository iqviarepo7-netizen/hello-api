from fastapi import FastAPI

app = FastAPI()

# Existing routes can be defined above or below this comment

@app.get("/hello", response_model=dict)
async def hello() -> dict:
    """Return a simple greeting message.

    Returns
    -------
    dict
        A JSON object with a single key ``message`` containing the greeting.
    """
    return {"message": "Hello, World!"}
