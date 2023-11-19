
class User:
  def __init__(self, id, name, address):
    self.id = id
    self.name = name
    self.address = address

  def __str__(self):
    return f"User {self.id}: {self.name}, {self.address}"
    
class Product:
  def __init__(self, id, name, price, quantity):
    self.id = id 
    self.name = name
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return f"Product {self.id}: {self.name}, ${self.price}, {self.quantity} left"
    
class Order:
  def __init__(self, id, user, products=[]):
    self.id = id
    self.user = user
    self.products = products
    self.totalPrice = 0

  def addProduct(self, product):
    self.products.append(product)
    
  def calculateTotal(self):
    self.totalPrice = sum(p.price for p in self.products)
    
  def __str__(self):
    return f"Order {self.id}, user: {self.user.name}, total: {self.totalPrice}"
    
class Payment:
    def __init__(self, id, amount, status="pending"):
        self.id = id
        self.amount = amount 
        self.status = status

    def pay(self):
        self.status = "paid"
    
    def confirm(self):
        print(f"Payment {self.id} for ${self.amount} confirmed")

#####
user1 = User(1, "John Doe", "123 St")  
product1 = Product(1, "Shirt", 10, 5)

order1 = Order(1, user1)
order1.addProduct(product1) 
order1.calculateTotal()

print(order1)
print(user1) 
print(product1)