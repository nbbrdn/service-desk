from app.services.health import HealthService


def test_health_service() -> None:
    service = HealthService()
    status = service.get_status()
    assert status == "ok"
