class Item:
    pay_rate = 0.8 # This is a class variable
    all = []
    def __init__(self, name:str, price: float, quantity=0):
        assert price>=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} isnot greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.quantity

    def __repr__(self): # To provide a developer friendly string representation of a object
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 1)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.all)
