
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        customer.orders.append(self)
        coffee.orders.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception ("Price must be a number between 1 and 10, inclusive")
            
    def __repr__(self) -> str:
         return f"<Order for {self.customer} - {self.coffee} - {self.price}>"