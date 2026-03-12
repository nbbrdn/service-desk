from app.core.config import settings


def test_settings_defaults() -> None:
    assert isinstance(settings.app_name, str)
    assert isinstance(settings.app_version, str)
    assert isinstance(settings.app_description, str)
    assert isinstance(settings.debug, bool)
