from app.repositories.product_repository import ProductRepository
from app.repositories.cart_repository import CartRepository
from app.services.product_service import ProductService
from app.services.cart_service import CartService

product_repository = ProductRepository()
cart_repository = CartRepository()

product_service = ProductService(product_repository)
cart_service = CartService(cart_repository, product_repository)
