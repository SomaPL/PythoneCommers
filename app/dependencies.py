from app.repositories.product_repository import ProductRepository
from app.repositories.cart_repository import CartRepository
from app.services.product_service import ProductService
from app.services.cart_service import CartService
from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService

product_repository = ProductRepository()
cart_repository = CartRepository()

product_service = ProductService(product_repository)
cart_service = CartService(cart_repository, product_repository)

order_repository = OrderRepository()
order_service = OrderService(
    order_repository=order_repository,
    cart_repository=cart_repository,
    product_repository=product_repository
)
