from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world", response_model=dict)
async def hello_world():
    return {"message": "Hello, World!"}
