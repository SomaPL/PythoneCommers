import pytest
from app.services.order_service import OrderService
from app.repositories.order_repository import OrderRepository
from app.repositories.cart_repository import CartRepository
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService
from app.services.cart_service import CartService


def create_order_service():
    product_repository = ProductRepository()
    cart_repository = CartRepository()
    order_repository = OrderRepository()

    product_service = ProductService(product_repository)
    cart_service = CartService(cart_repository, product_repository)

    order_service = OrderService(
        order_repository=order_repository,
        cart_repository=cart_repository,
        product_repository=product_repository,
    )

    return order_service, product_service, cart_service


def test_create_order_success():
    order_service, product_service, cart_service = create_order_service()

    product_service.create_product(1, "Keyboard", 199.99, 10)
    cart_service.add_to_cart(user_id=1, product_id=1, quantity=2)

    order = order_service.create_order(user_id=1)

    assert order.id == 1
    assert order.user_id == 1
    assert order.total_price == 399.98
    assert order.status == "CREATED"
    assert len(order.items) == 1
    assert order.items[0].product_id == 1
    assert order.items[0].quantity == 2


def test_create_order_empty_cart_raises_error():
    order_service, _, _ = create_order_service()

    with pytest.raises(ValueError):
        order_service.create_order(user_id=1)
