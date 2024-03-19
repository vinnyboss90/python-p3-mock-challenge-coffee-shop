class Customer:

    all = []

    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception
        if not 1 <= len(value) <= 15:
            raise Exception
        self._name = value

    def orders(self):
        return [order for order in Order.all if isinstance(order, Order) and order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders() if isinstance(order.coffee, Coffee)})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Coffee:

    all = []

    def __init__(self, name):
        self._name = None
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name is None:
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
            else:
                raise ValueError(
                    "Name must be a string greater than 2 characters")
        else:
            raise AttributeError("Cannot change the name after initialization")

    def orders(self):
        return [order for order in Order.all if isinstance(order, Order) and order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders() if isinstance(order.customer, Customer)})

    def num_orders(self):
        times_ordered = 0

        for order in Order.all:
            if order.coffee == self:
                times_ordered += 1

        return times_ordered

    @staticmethod
    def average_price():
        total_orders = len(Order.all)
        if total_orders == 0:
            return 0.0

        total_price = sum(order.price for order in Order.all)
        average_price = total_price / total_orders

        rounded_average = round(average_price, 1)
        return rounded_average


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer):
            self.customer = customer
        if isinstance(coffee, Coffee):
            self.coffee = coffee
        self._price = None
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if self._price is None:
            if isinstance(price, float) and 1.0 <= price <= 10.0:
                self._price = price
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0")
        else:
            raise Exception
