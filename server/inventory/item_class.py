class Item:

    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price} - {self.quantity} left"
    
    def update_quantity(self, burn_rate):
        self.quantity = self.quantity - (self.quantity * burn_rate)
        return self.quantity
    
    