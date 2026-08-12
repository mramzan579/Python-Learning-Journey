#cart class with currency as class variable and name, price, items as instance variables. Add a method to add items to the cart and a method to calculate total price of items in the cart. Create two instances of the cart class and add items to them. Print the total price of items in each cart along with the currency.
class cart():
    currency='PKR'
    def __init__(self, name, price):
        self.name=name
        self.price=price
        self.items=[]
    def add_items(self, item, price):
        self.items.append((item, price))
    def total_price(self):
        return sum(item[1] for item in self.items)
assert cart.currency == "PKR"
my_cart=cart('My Cart', 0)
your_cart=cart('Your Cart', 0)
my_cart.add_items('apple', 10)
my_cart.add_items('banana', 5)
print(f"{my_cart.name} total price: {my_cart.total_price()} {cart.currency}")

