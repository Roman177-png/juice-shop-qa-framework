import pytest

from src.api.users_service import UsersService
from src.data.user_factory import build_registration_request
from src.models.user import SecurityQuestion, UserRegistrationRequest


@pytest.mark.api
def test_user_can_register_with_valid_data(
    users_service: UsersService, registration_request: UserRegistrationRequest
) -> None:
    response = users_service.register(registration_request)

    assert response.status == 201
    assert response.json()["data"]["email"] == registration_request.email


@pytest.mark.api
def test_registration_fails_when_passwords_do_not_match(
    users_service: UsersService, security_question: SecurityQuestion
) -> None:
    payload = build_registration_request(security_question)
    mismatched = payload.model_copy(update={"password_repeat": f"{payload.password}-mismatch"})

    response = users_service.register(mismatched)

    assert response.status == 400


@pytest.mark.api
def test_registration_fails_with_duplicate_email(
    users_service: UsersService,
    registered_user: UserRegistrationRequest,
    security_question: SecurityQuestion,
) -> None:
    duplicate = build_registration_request(security_question).model_copy(
        update={"email": registered_user.email}
    )

    response = users_service.register(duplicate)

    assert response.status == 400


@pytest.mark.api
def test_registration_fails_with_invalid_email_format(
    users_service: UsersService, security_question: SecurityQuestion
) -> None:
    payload = build_registration_request(security_question).model_copy(
        update={"email": "not-an-email"}
    )

    response = users_service.register(payload)

    assert response.status == 400
