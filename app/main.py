from fastapi import FastAPI

app = FastAPI()

# Existing routes (if any) would be here

@app.get("/hello_world_i_am_mk", response_model=dict)
def hello_world_i_am_mk():
    return {"message": "Hello, world! I am mk"}
