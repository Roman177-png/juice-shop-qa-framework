from collections.abc import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from src.api.client import ApiClient
from src.api.products_service import ProductsService
from src.api.users_service import UsersService
from src.data.user_factory import build_registration_request
from src.models.common import Envelope
from src.models.user import SecurityQuestion, UserRegistrationRequest


@pytest.fixture
def request_context(playwright: Playwright, base_url: str) -> Generator[APIRequestContext, None, None]:
    context = playwright.request.new_context(base_url=base_url)
    yield context
    context.dispose()


@pytest.fixture
def api_client(request_context: APIRequestContext) -> ApiClient:
    return ApiClient(request_context)


@pytest.fixture
def users_service(api_client: ApiClient) -> UsersService:
    return UsersService(api_client)


@pytest.fixture
def products_service(api_client: ApiClient) -> ProductsService:
    return ProductsService(api_client)


@pytest.fixture
def security_question(users_service: UsersService) -> SecurityQuestion:
    response = users_service.get_security_questions()
    envelope = Envelope[list[SecurityQuestion]].model_validate(response.json())
    return envelope.data[0]


@pytest.fixture
def registration_request(security_question: SecurityQuestion) -> UserRegistrationRequest:
    return build_registration_request(security_question)


@pytest.fixture
def registered_user(
    users_service: UsersService, registration_request: UserRegistrationRequest
) -> UserRegistrationRequest:
    response = users_service.register(registration_request)
    assert response.status == 201
    return registration_request
