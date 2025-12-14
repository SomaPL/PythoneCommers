from typing import List, Optional
from app.models.product import Product


class ProductRepository:
    def __init__(self):
        self._products: List[Product] = []

    def add(self, product: Product) -> None:
        self._products.append(product)

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return next((p for p in self._products if p.id == product_id), None)
    
    def get_all(self) -> List[Product]:
        return self._products