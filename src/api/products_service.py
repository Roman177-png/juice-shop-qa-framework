from playwright.sync_api import APIResponse

from src.api.client import ApiClient


class ProductsService:
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def list_products(self) -> APIResponse:
        """List all storefront products."""
        return self._client.get("/rest/products")

    def get_product(self, product_id: int) -> APIResponse:
        """Fetch a single product by its id."""
        return self._client.get(f"/api/Products/{product_id}")

    def create_product(self, payload: dict[str, object], *, token: str | None = None) -> APIResponse:
        """Create a product, optionally authenticated with a bearer token."""
        headers = {"Authorization": f"Bearer {token}"} if token else None
        return self._client.post("/api/Products", json=payload, headers=headers)
