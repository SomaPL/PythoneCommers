from datetime import datetime
from app.models.order import Order
from app.models.order_item import OrderItem
from app.repositories.order_repository import OrderRepository
from app.repositories.cart_repository import CartRepository
from app.repositories.product_repository import ProductRepository

class OrderService:
    def __init__(
        self,
        order_repository: OrderRepository,
        cart_repository: CartRepository,
        product_repository: ProductRepository,
    ) -> None:
        self._order_repository = order_repository
        self._cart_repository = cart_repository
        self._product_repository = product_repository
        self._next_order_id = 1

    def create_order(self, user_id: int) ->Order:
        cart = self._cart_repository.get_by_user_id(user_id)
        if cart is None or not cart.items:
            raise ValueError("Cart is empty or does not exist")
        
        order_items: list[OrderItem] = []
        total_price = 0.0

        for item in cart.items:
            product = self._product_repository.get_by_id(item.product_id)
            if product is None:
                raise ValueError(f"Product with ID {item.product_id} does not exist")
            if product.stock_quantity < item.quantity:
                raise ValueError(f"Insufficient stock for product ID {item.product_id}")
            
            product.stock_quantity -= item.quantity

            order_item = OrderItem(
                product_id =product.id,
                product_name=product.name,
                quantity=item.quantity,
                unit_price=product.price,
            )
            order_items.append(order_item)
            total_price += product.price * item.quantity

        order = Order(
            id=self._next_order_id,
            user_id=user_id,
            items=order_items,
            total_price=total_price,
            status="CREATED",
            created_at=datetime.utcnow(),
        )
        self._next_order_id += 1
        self._order_repository.add(order)
        self._cart_repository.delete(user_id)

        return order
    
    def get_order(self, order_id: int) -> Order | None:
        return self._order_repository.get_by_id(order_id)