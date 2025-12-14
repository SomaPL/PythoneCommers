from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.models.order_item import OrderItem

class Order(BaseModel):
    id:int
    user_id:int
    items:List[OrderItem]
    total_price:float
    status:str
    created_at:datetime
    






    