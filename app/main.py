from fastapi import FastAPI

app = FastAPI()


@app.get("/hello", response_model=dict)
async def hello() -> dict:
    """Return a simple greeting message.

    Returns
    -------
    dict
        A JSON object with a greeting message.
    """
    return {"message": "Hello, World!"}
