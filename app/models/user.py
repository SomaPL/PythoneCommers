from pydantic import BaseModel
from pydantic import EmailStr

class User(BaseModel):
    id: int
    email: EmailStr
    name: str
