from src.product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def remove_product(self, product: Product):
        if product in self.__products:
            self.__products.remove(product)

    def get_total_price(self) -> float:
        total_price = 0.0
        for product in self.__products:
            total_price += product.get_price()
        return total_price

    def display_cart(self):
        print("Shopping Cart:")
        for product in self.__products:
            print(f"- {product.get_name()}: ${product.get_price()}")