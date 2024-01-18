class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception ("Coffee name must be a string")
    
    def get_customers(self):
        customers = []
        for order in self.orders:
            if order.coffee == self:
                customers.append(order.customer)
        return customers
    
    def num_orders(self): # Returns the total number of times that coffee has been ordered
        return len(self.orders)
    
    def average_price(self): # Returns the average price for a coffee based on its orders
        # coffee_prices = []
        # for order in self.orders:
        #     coffee_prices.append(order.price)
        # return sum(coffee_prices) / len(coffee_prices)
    
        return sum([order.price for order in self.orders]) / self.num_orders()

    def __repr__(self) -> str:
        return f"<Coffee {self.name}>"