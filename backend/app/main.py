from fastapi import FastAPI

# Import routers
from .routers import patients
from .routers import hello_world

app = FastAPI()

# Include routers
app.include_router(patients.router)
app.include_router(hello_world.router)
