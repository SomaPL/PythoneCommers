from xml.etree.ElementTree import Element,SubElement,tostring
from app.models.order import Order

def order_to_xml(order: Order) -> str:
    order_el = Element("order")

    SubElement(order_el, "id").text = str(order.id)
    SubElement(order_el, "user_id").text = str(order.user_id)
    SubElement(order_el, "status").text = order.status
    SubElement(order_el, "total_price").text = str(order.total_price)
    SubElement(order_el, "created_at").text = order.created_at.isoformat()

    items_el = SubElement(order_el, "items")
    for item in order.items:
        item_el = SubElement(items_el, "item")
        SubElement(item_el, "product_id").text = str(item.product_id)
        SubElement(item_el, "product_name").text = item.product_name
        SubElement(item_el, "quantity").text = str(item.quantity)
        SubElement(item_el, "unit_price").text = str(item.unit_price)

    return tostring(order_el, encoding="unicode")