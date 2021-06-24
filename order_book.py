from collections import namedtuple
from heapq import heappop, heappush
from typing import Optional


class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def process_order(self, order_type, price) -> Optional[float]:
        if order_type == 1:
            if self.sell_orders and self.sell_orders[0] <= price:
                return heappop(self.sell_orders)
            else:
                heappush(self.buy_orders, - price)
        elif order_type == -1:
            if self.buy_orders and - self.buy_orders[0] >= price:
                return - heappop(self.buy_orders)
            else:
                heappush(self.sell_orders, price)
