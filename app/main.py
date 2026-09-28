from fastapi import FastAPI

app = FastAPI()

@app.get("/run-pipeline")
async def run_pipeline():
    """Endpoint triggered by Run Pipeline button.
    Returns a JSON payload with a welcome message.
    """
    return {"message": "Welcome home"}
