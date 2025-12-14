from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.repositories.cart_repository import CartRepository
from app.repositories.product_repository import ProductRepository


class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository) -> None:
        self._cart_repository = cart_repository
        self._product_repository = product_repository

    def get_cart(self, user_id: int) -> Cart:
        cart = self._cart_repository.get_by_user_id(user_id)
        if cart is None:
            cart = Cart(user_id=user_id, items=[])
            self._cart_repository.save(cart)
        return cart
    
    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> Cart:
        product = self._product_repository.get_by_id(product_id)
        if product is None:
            raise ValueError("Product not found")
        
        cart = self.get_cart(user_id)

        for item in cart.items:
            if item.product_id == product_id:
                item.quantity += quantity
                self._cart_repository.save(cart)
                return cart
        
        cart.items.append(CartItem(product_id=product_id, quantity=quantity))
        self._cart_repository.save(cart)
        return cart
    
    def clear_cart(self, user_id: int) -> None:
        self._cart_repository.delete(user_id)