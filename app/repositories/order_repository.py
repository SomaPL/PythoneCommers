from typing import List, Optional
from app.models.order import Order

class OrderRepository:
    def __init__(self):
        self._orders: List[Order] = []

    def add(self, order:Order) -> None:
        self._orders.append(order)

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return next((o for o in self._orders if o.id == order_id), None)
    
    def get_all(self) -> List[Order]:
        return self._orders