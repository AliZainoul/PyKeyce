from src.product import Product
from src.shopping_cart import ShoppingCart
from src.customer import Customer

# Usage example
product1 = Product(1, "Product 1", 10.99)
product2 = Product(2, "Product 2", 19.99)

customer = Customer("John")
customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.remove_from_cart(product1)
customer.checkout()
#customer.__cart.display_cart()  # Attempting to access the private cart attribute
