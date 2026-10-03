from fastapi import FastAPI

app = FastAPI()

# Existing routes may be defined below

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}
