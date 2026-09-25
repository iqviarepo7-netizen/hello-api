from fastapi import FastAPI

app = FastAPI()

@app.post("/run-pipeline")
async def run_pipeline():
    """Endpoint triggered by the Run Pipeline button.
    Returns a JSON payload that the front‑end can use to display a modal
    with the text "welcome home".
    """
    return {"popup": "welcome home"}
