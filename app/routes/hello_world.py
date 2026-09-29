from fastapi import APIRouter

router = APIRouter()


@router.get("/", name="root")
async def read_root():
    """Simple health‑check endpoint returning a greeting.
    """
    return {"message": "Hello, World!"}
