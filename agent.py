from typing import List, Tuple, Optional
import numpy as np


class Agent:
    personal_infos = []

    def __init__(self, price_history_len):
        self.order = None
        self.price_history_len = price_history_len

    def update(self, price_history: List[float], info: float, fundamental: float) -> Optional[Tuple[int, float]]:
        raise NotImplementedError()


class NoiseAgent(Agent):
    def __init__(self,
                 sentiment,
                 reaction_strength,
                 order_period,
                 info_var_squared,
                 price_history_len):
        Agent.__init__(self, price_history_len)
        self.sentiment = sentiment
        self.reaction_strength = reaction_strength
        self.order_period = order_period
        self.info_var_squared = info_var_squared
        self.threshold = 0

    def update(self, price_history: List[float], info: float, fundamental: float):
        personal_info = info + self.sentiment
        Agent.personal_infos.append(personal_info)
        if abs(personal_info) < self.threshold:
            self.threshold -= 2 * self.info_var_squared / self.order_period
            return None
        else:
            self.threshold = 2 * self.info_var_squared
            self.order = (np.sign(personal_info), price_history[-1] + self.reaction_strength * personal_info)
            return self.order


class BuyAgent(Agent):
    def __init__(self, order_period: int, buy_price_mult, price_history_len: int):
        Agent.__init__(self, price_history_len)
        self.order_period = order_period
        self.price_mult = buy_price_mult
        self.counter = 0

    def update(self, price_history: List[float], info: float, fundamental: float) -> Optional[Tuple[int, float]]:
        if not self.counter:
            self.order = (1, self.price_mult * price_history[-1])
            self.counter = self.order_period
            return self.order
        self.counter -= 1
