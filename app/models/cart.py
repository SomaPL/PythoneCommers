from pydantic import BaseModel
from typing import List
from app.models.cart_item import CartItem


class Cart(BaseModel):
    user_id: int
    items: List[CartItem] = []