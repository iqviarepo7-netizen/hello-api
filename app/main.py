from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_fallback", response_model=dict)
def hello_fallback():
    return {"message": "Hello from fallback"}
