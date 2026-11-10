from playwright.sync_api import APIRequestContext, APIResponse


class ApiClient:
    def __init__(self, request_context: APIRequestContext) -> None:
        self._context = request_context

    def get(self, path: str, **kwargs: object) -> APIResponse:
        """Send a GET request to the given path."""
        return self._context.get(path, **kwargs)  # type: ignore[arg-type]

    def post(self, path: str, **kwargs: object) -> APIResponse:
        """Send a POST request to the given path."""
        return self._context.post(path, **kwargs)  # type: ignore[arg-type]

    def put(self, path: str, **kwargs: object) -> APIResponse:
        """Send a PUT request to the given path."""
        return self._context.put(path, **kwargs)  # type: ignore[arg-type]

    def delete(self, path: str, **kwargs: object) -> APIResponse:
        """Send a DELETE request to the given path."""
        return self._context.delete(path, **kwargs)  # type: ignore[arg-type]
