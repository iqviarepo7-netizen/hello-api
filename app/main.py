from fastapi import FastAPI


def create_app() -> FastAPI:
    """Factory to create and configure the FastAPI application.

    This isolates side‑effects (like router imports) to runtime rather than import time,
    preventing circular‑import issues that caused the startup failure.
    """
    app = FastAPI()

    # Import routers lazily to avoid import‑time side effects
    from app.routes.hello_world import router as hello_world_router
    app.include_router(hello_world_router)

    return app


# The public ASGI application instance used by uvicorn and tests
app = create_app()
