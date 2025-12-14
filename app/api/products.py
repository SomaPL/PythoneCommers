from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository

router = APIRouter(prefix="/products", tags=["products"])

product_repository = ProductRepository()
product_service = ProductService(product_repository)

@router.post("/", response_model=Product)
def create_product(product: Product):
    create_product = product_service.create_product(
        product_id=product.id,
        name=product.name,
        price=product.price,
        stock_quantity=product.stock_quantity,
    )
    return create_product

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=list[Product])
def list_products():
    return product_service.list_products()