from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint returning a greeting message.

    Returns
    -------
    dict
        A JSON‑serializable dictionary containing a ``message`` key.
    """
    return {"message": "Hello, world!"}
