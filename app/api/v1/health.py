from fastapi import APIRouter

from app.api.dependencies import get_health_service
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    health_service = get_health_service()
    status = health_service.get_status()
    return HealthResponse(status=status)
