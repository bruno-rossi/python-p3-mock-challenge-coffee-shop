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
        orders_per_coffee = {}
        for order in self.orders:
            if self.name in orders_per_coffee:
                orders_per_coffee.update({self.name: orders_per_coffee.get(self.name) + 1})
            else:
                orders_per_coffee.update({self.name: 1})

        print(orders_per_coffee)
        print(orders_per_coffee[self.name])
        return orders_per_coffee[self.name]
    
    def average_price(self): # Returns the average price for a coffee based on its orders
        
        coffee_prices = []
        for order in self.orders:
            coffee_prices.append(order.price)
        return sum(coffee_prices) / len(coffee_prices)

    def __repr__(self) -> str:
        return f"<Coffee {self.name}>"