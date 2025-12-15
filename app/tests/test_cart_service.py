import pytest
from app.services.cart_service import CartService
from app.repositories.cart_repository import CartRepository
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService

def create_cart_service():
    product_repository = ProductRepository()
    cart_repository = CartRepository()

    product_service = ProductService(product_repository)
    cart_service = CartService(cart_repository, product_repository)
    return cart_service, product_service

def test_get_empty_cart_creates_new_cart():
    cart_service, _ = create_cart_service()

    cart = cart_service.get_cart(user_id=1)

    assert cart.user_id == 1
    assert len(cart.items) == 0

def test_add_product_to_cart():
    cart_service, product_service = create_cart_service()

    product_service.create_product(1, "Keyboard", 199.99, 10)

    cart_service.add_to_cart(user_id=1, product_id=1, quantity=1)
    cart = cart_service.add_to_cart(user_id=1, product_id=1, quantity=3)

    assert len(cart.items) == 1
    assert cart.items[0].quantity == 4

def test_add_same_product_twice_increases_quantity():
    cart_service, product_service = create_cart_service()

    product_service.create_product(1, "Mouse", 99.99, 20)

    cart_service.add_to_cart(user_id=1, product_id=1, quantity=1)
    cart = cart_service.add_to_cart(user_id=1, product_id=1, quantity=3)

    assert len(cart.items) == 1
    assert cart.items[0].quantity == 4

def test_add_non_existing_product_raises_error():
    cart_service, _ = create_cart_service()

    with pytest.raises(ValueError):
        cart_service.add_to_cart(user_id=1, product_id=999, quantity=1)


def test_clear_cart():
    cart_service, product_service = create_cart_service()

    product_service.create_product(1, "Monitor", 899.99, 5)
    cart_service.add_to_cart(user_id=1, product_id=1, quantity=1)

    cart_service.clear_cart(user_id=1)
    cart = cart_service.get_cart(user_id=1)

    assert cart.items == []