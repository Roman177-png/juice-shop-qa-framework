import pytest

from src.utils.settings import Settings, get_settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    return get_settings()


@pytest.fixture(scope="session")
def base_url(settings: Settings) -> str:
    return str(settings.base_url).rstrip("/")


@pytest.fixture
def browser_context_args(browser_context_args: dict[str, object]) -> dict[str, object]:
    return {**browser_context_args, "viewport": {"width": 1440, "height": 900}}
