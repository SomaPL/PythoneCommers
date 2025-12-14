from pydantic import BaseModel
from pydantic import Field

class CartItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)