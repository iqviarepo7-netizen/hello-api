from fastapi import FastAPI

app = FastAPI()

@app.get("/hello", response_model=dict)
async def hello():
    return {"message": "Hello, World!"}
