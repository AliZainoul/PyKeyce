from src.product import Product
from src.shopping_cart import ShoppingCart
from src.customer import Customer

# Usage example

products = []
for i in range(1, 10):
    if i % 5 == 1:
        product = Product(i, f"Product {i}", 10.75)
        products.append(product)
    else:
        product = Product(i, f"Product {i}", 5.25)
        products.append(product)

customer = Customer("John")

for product in products:
    customer.add_to_cart(product)  # Add products to the customer's cart

product1 = products[-1]
customer.remove_from_cart(product1)  # Remove a product from the cart

customer.checkout()  # Proceed to checkout



# Attempting to access the private cart attribute
# customer.__cart.display_cart()  # This line will raise an AttributeError