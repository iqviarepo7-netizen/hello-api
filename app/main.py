from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_vanakam")
async def hello_vanakam():
    return {"message": "Vanakam!"}
