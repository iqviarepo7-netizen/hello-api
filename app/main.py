from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_world", response_model=dict)
async def hello_world() -> dict:
    """Return a simple greeting message.

    Returns
    -------
    dict
        A dictionary with a single key ``message`` containing the greeting.
    """
    return {"message": "Hello, World!"}
