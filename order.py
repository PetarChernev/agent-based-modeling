class Order:
    def __init__(self, agent, order_type, price):
        self.agent = agent
        self.type = order_type
        self.price = price

    def __lt__(self, other):
        return self.type * self.price > self.type * other.price

    def __le__(self, other):
        return self.type * self.price >= self.type * other.price

    def __gt__(self, other):
        return self.type * self.price < self.type * other.price

    def __ge__(self, other):
        return self.type * self.price <= self.type * other.price

    def __eq__(self, other):
        return self.type * self.price == self.type * other.price

    def __repr__(self):
        return str((self.type, self.price))

    def fulfill(self):
        self.agent.shares += self.type
        self.agent.capital += -self.type * self.price
