from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world")
async def hello_world():
    return {"message": "Hello, world!"}

# New endpoint as per SCRUM-9
@app.get("/hello_hi")
async def hello_hi():
    return {"message": "Hello, hi!"}
