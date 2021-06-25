from collections import namedtuple
from heapq import heappop, heappush
from typing import Optional


class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def process_order(self, order) -> Optional[float]:
        if order.type == 1:
            if self.sell_orders and self.sell_orders[0] <= order:
                sell_order = heappop(self.sell_orders)
                # sell_order.fulfill()
                # order.fulfill()
                return order.price
            else:
                heappush(self.buy_orders, order)
        elif order.type == -1:
            if self.buy_orders and self.buy_orders[0] <= order:
                buy_order = heappop(self.buy_orders)
                # buy_order.fulfill()
                # order.fulfill()
                return order.price
            else:
                heappush(self.sell_orders, order)
