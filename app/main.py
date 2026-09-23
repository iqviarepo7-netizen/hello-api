from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_fallback")
async def hello_fallback():
    return {"message": "Hello, world!"}

@app.get("/hello_vanakam_enaku_saaaavee_illai")
async def hello_vanakam():
    return {"message": "Vanakam, enaku saaavee illai"}
