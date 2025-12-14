from typing import Dict, Optional
from app.models.cart import Cart

class CartRepository:
    def __init__ (self):
        self._carts: Dict[int, Cart] = {}

    def get_by_user_id(self, user_id: int) ->Optional[Cart]:
        return self._carts.get(user_id)
    
    def save(self, cart: Cart) -> None:
        self._carts[cart.user_id] = cart

    def delete(self, user_id: int) -> None:
        self._carts.pop(user_id, None)
