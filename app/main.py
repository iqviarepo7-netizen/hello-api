from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .auth import verify_credentials

app = FastAPI()

# Mount static and templates if they exist
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class LoginRequest(BaseModel):
    email: str
    password: str


@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(req: LoginRequest):
    if verify_credentials(req.email, req.password):
        return {"detail": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Existing hello world endpoint (preserve original behavior)
@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
