from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_fallback")
async def hello_fallback():
    return {"message": "Hello, world!"}
