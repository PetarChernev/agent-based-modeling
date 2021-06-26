from typing import List, Tuple, Optional
import numpy as np

from order import Order


class Agent:
    personal_infos = []

    def __init__(self, shares, capital, price_history_len):
        self.order = None
        self.shares = shares
        self.capital = capital
        self.price_history_len = price_history_len

    def update(self, price_history: List[float], info: float, fundamental: float) -> Optional[Tuple[int, float]]:
        raise NotImplementedError()


class NoiseAgent(Agent):
    def __init__(self,
                 shares,
                 capital,
                 sentiment,
                 reaction_strength,
                 order_period,
                 info_var_squared,
                 price_history_len):
        Agent.__init__(self, shares, capital, price_history_len)
        self.sentiment = sentiment
        self.reaction_strength = reaction_strength
        self.order_period = order_period
        self.info_var_squared = info_var_squared
        self.threshold = 0

    def update(self, price_history: List[float], info: float, fundamental: float):
        personal_info = info + self.sentiment
        Agent.personal_infos.append(personal_info)
        if abs(personal_info) > self.threshold:
            # wants to place a new order
            self.threshold = 2 * self.info_var_squared
            order_type = np.sign(personal_info)
            # can't place sell order with no held shares and buy order with negative capital:
            #if (order_type == -1 and self.shares) or (order_type == 1 and self.capital > 0):
            return Order(agent=self,
                         order_type=order_type,
                         price=price_history[-1] + self.reaction_strength * personal_info)
        else:
            self.threshold -= 2 * self.info_var_squared * self.order_period
            return None
