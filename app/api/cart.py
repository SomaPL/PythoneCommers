from fastapi import APIRouter
from pydantic import BaseModel
from app.services.cart_service import CartService
from app.services.product_service import ProductService
from app.repositories.cart_repository import CartRepository
from app.repositories.product_repository import ProductRepository
from app.dependencies import cart_service, product_service

router = APIRouter(prefix="/cart", tags=["cart"])



class AddToCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int

@router.get("/{user_id}")
def get_cart(user_id: int):
    return cart_service.get_cart(user_id)

@router.post("/add")
def add_to_cart(request: AddToCartRequest):
    return cart_service.add_to_cart(
        user_id=request.user_id,
        product_id=request.product_id,
        quantity=request.quantity
    )

@router.post("/_debug_add_product")
def debug_add_product():
    product_service.create_product(1, "Test Product", 10.0, 10)
    return {"status": "ok"}
