from playwright.sync_api import APIResponse

from src.api.client import ApiClient
from src.models.user import LoginRequest, UserRegistrationRequest


class UsersService:
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def get_security_questions(self) -> APIResponse:
        """Fetch the list of security questions offered during registration."""
        return self._client.get("/api/SecurityQuestions")

    def register(self, payload: UserRegistrationRequest) -> APIResponse:
        """Register a new user account."""
        return self._client.post("/api/Users", json=payload.model_dump(mode="json", by_alias=True))

    def login(self, payload: LoginRequest) -> APIResponse:
        """Authenticate a user and obtain a JWT."""
        return self._client.post("/rest/user/login", json=payload.model_dump(mode="json"))
