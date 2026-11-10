import pytest

from src.api.users_service import UsersService
from src.models.user import LoginRequest, LoginResponse, UserRegistrationRequest


@pytest.mark.api
def test_user_can_login_with_valid_credentials(
    users_service: UsersService, registered_user: UserRegistrationRequest
) -> None:
    response = users_service.login(
        LoginRequest(email=registered_user.email, password=registered_user.password)
    )

    assert response.status == 200
    login_response = LoginResponse.model_validate(response.json())
    assert login_response.authentication.token


@pytest.mark.api
def test_login_fails_with_wrong_password(
    users_service: UsersService, registered_user: UserRegistrationRequest
) -> None:
    response = users_service.login(
        LoginRequest(email=registered_user.email, password="wrong-password")
    )

    assert response.status == 401


@pytest.mark.api
def test_login_fails_with_unknown_email(users_service: UsersService) -> None:
    response = users_service.login(
        LoginRequest(email="unknown-user@example.com", password="whatever")
    )

    assert response.status == 401
