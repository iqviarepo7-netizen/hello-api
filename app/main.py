from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world")
async def hello_world():
    return {"message": "Hello, world!"}

# New fallback endpoint
@app.get("/hello_fallback")
async def hello_fallback():
    return {"message": "Hello from fallback"}
