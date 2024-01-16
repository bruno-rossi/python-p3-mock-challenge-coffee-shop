class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name
        else:
            raise Exception ("Name must be a string between 1 and 15 characters")
    
    def get_coffees(self):
        coffees = []
        for order in self.orders:
            if order.customer == self:
                coffees.append(order.coffee)
        return coffees

    def __repr__(self) -> str:
        return f"<Customer {self.name}>"