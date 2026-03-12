from fastapi import FastAPI

from app.api.v1 import router as v1_router
from app.core.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.debug,
)

app.include_router(v1_router, prefix="/api/v1")
