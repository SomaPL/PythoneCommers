from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def create_product(self, product_id: int, name: str, price: float, stock_quantity: int) -> Product:
        product = Product(
            id=product_id,
            name=name,
            price=price,
            stock_quantity=stock_quantity
        )
        self._product_repository.add(product)
        return product

    def get_product(self, product_id: int) -> Product | None:
        return self._product_repository.get_by_id(product_id)
    
    def list_products(self) -> list[Product]:
        return self._product_repository.get_all()
    
    def decrease_stock(self, product_id: int, quantity: int) -> None:
        product = self._product_repository.get_by_id(product_id)
        if product is None:
            raise ValueError("Product not found")
        if product.stock_quantity < quantity:
            raise ValueError("Insufficient stock")
        product.stock_quantity -= quantity

    
