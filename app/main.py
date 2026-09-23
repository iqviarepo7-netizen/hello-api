from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello_world_i_am_mk")
async def hello_world_i_am_mk():
    return JSONResponse(content={"message": "Hello, world! I am mk"})
