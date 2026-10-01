from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello_world_i_am_mk")
def hello_world_i_am_mk():
    return {"message": "Hello world, I am MK"}


@app.get("/")
def read_root():
    return {"Hello": "World"}
