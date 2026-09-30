from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import connect_client, disconnect_client
from app.routers import patients


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_client()
    yield
    disconnect_client()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:1697",
        "http://127.0.0.1:1697",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patients.router, prefix="/api")


@app.get("/hello_world_i_am_mk")
def hello_world():
    return {"message": "Hello World, I am MK"}
