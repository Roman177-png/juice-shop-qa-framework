from faker import Faker

from src.models.user import SecurityQuestion, UserRegistrationRequest

_faker = Faker()


def build_registration_request(
    security_question: SecurityQuestion, *, password: str | None = None
) -> UserRegistrationRequest:
    chosen_password = password or _faker.password(length=12)
    return UserRegistrationRequest(
        email=_faker.unique.email(),
        password=chosen_password,
        password_repeat=chosen_password,
        security_question=security_question,
        security_answer=_faker.word(),
    )
