import pytest

from src.api.products_service import ProductsService
from src.models.common import Envelope
from src.models.product import Product


@pytest.mark.api
def test_get_products_returns_a_non_empty_list(products_service: ProductsService) -> None:
    response = products_service.list_products()

    assert response.status == 200
    envelope = Envelope[list[Product]].model_validate(response.json())
    assert len(envelope.data) > 0


@pytest.mark.api
def test_get_product_by_id_returns_matching_product(products_service: ProductsService) -> None:
    listing = Envelope[list[Product]].model_validate(products_service.list_products().json())
    existing_id = listing.data[0].id

    response = products_service.get_product(existing_id)

    assert response.status == 200
    product = Envelope[Product].model_validate(response.json()).data
    assert product.id == existing_id


@pytest.mark.api
def test_get_product_by_unknown_id_returns_404(products_service: ProductsService) -> None:
    response = products_service.get_product(999_999)

    assert response.status == 404


@pytest.mark.api
def test_create_product_without_authentication_returns_401(
    products_service: ProductsService,
) -> None:
    response = products_service.create_product({"name": "Hacked Juice", "price": 1})

    assert response.status == 401
