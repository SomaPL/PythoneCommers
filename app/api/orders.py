from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from app.models.order import Order
from app.dependencies import order_service
from app.utils.order_xml import order_to_xml


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/{user_id}", response_model=Order)
def create_order(user_id: int):
    try:
        return order_service.create_order(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    order = order_service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/{order_id}/xml",)
def get_order_xml(order_id: int):
    order = order_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    xml_data = order_to_xml(order)
    return Response(content=xml_data, media_type="application/xml")