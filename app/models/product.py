from pydantic import BaseModel
from pydantic import Field

class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)
    stock_quantity: int = Field(ge=0)