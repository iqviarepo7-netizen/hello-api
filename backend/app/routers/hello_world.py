from fastapi import APIRouter

router = APIRouter(prefix="/hello_world_i_am_mk")

@router.get("", response_model=dict)
async def hello_world():
    return {"message": "Hello, world!"}
