import pytest
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository

def create_service():
    repository = ProductRepository()
    service = ProductService(repository)
    return service

def test_create_product():
    service = create_service()

    product = service.create_product(
        product_id=1,
        name="Mouse",
        price=29.99,
        stock_quantity=20
    )
    assert product.id == 1
    assert product.name == "Mouse"
    assert product.price == 29.99
    assert product.stock_quantity == 20

def test_list_products():
    service = create_service()

    service.create_product(1, "Keyboard", 199.99, 10)
    service.create_product(2, "Mouse", 99.99, 20)

    products = service.list_products()

    assert len(products) == 2

def test_decrease_stock():
    service = create_service()

    service.create_product(1, "Monitor", 899.99, 5)
    service.decrease_stock(1, 2)

    product = service.get_product(1)
    assert product.stock_quantity == 3 # type: ignore

def test_get_product_by_id():
    service = create_service()

    service.create_product(1, "Keyboard", 199.99, 1)
    service.create_product(2, "Mouse", 99.99, 20)

    products = service.list_products()
    
    assert len(products) == 2

def test_decrease_stock_not_enough_quantity():
    service = create_service()

    service.create_product(1, "Monitor", 899.99, 1)

    with pytest.raises(ValueError):
        service.decrease_stock(1, 5)


def test_decrease_stock_product_not_found():
    service = create_service()

    with pytest.raises(ValueError):
        service.decrease_stock(999, 1)