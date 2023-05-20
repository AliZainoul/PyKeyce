from src.product import Product
from src.shopping_cart import ShoppingCart


class Customer:
    def __init__(self, name: str):
        self.__name = name
        self.__cart = ShoppingCart()

    def add_to_cart(self, product: Product):
        self.__cart.add_product(product)

    def remove_from_cart(self, product: Product):
        self.__cart.remove_product(product)

    def checkout(self):
        total_price = self.__cart.get_total_price()
        print(f"Checking out... Total Price: ${total_price:.2f}")
