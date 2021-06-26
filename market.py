import numpy as np

from order_book import OrderBook
from market_data import MarketData


class Market:
    def __init__(self, info_var_squared, fundamental_change_var_squared):
        self.info_var_sq = info_var_squared
        self.fundamental_change_var_sq = fundamental_change_var_squared

    def simulate(self, agents, max_t, initial_price):
        info_series = np.random.normal(0, self.info_var_sq, max_t)
        fundamental_series = np.cumsum(np.random.normal(0, self.fundamental_change_var_sq, max_t))
        order_book = OrderBook()

        s = [initial_price]
        b = [initial_price]
        p = [initial_price]
        number_of_buys = [0]
        number_of_sells = [0]
        spread = [0]
        fulfilled_buys_series = [0]
        fulfilled_sells_series = [0]
        for i in range(max_t):
            fulfilled_buys = 0
            fulfilled_sells = 0
            if not i % (max_t//100):
                print(f"t={i}/{max_t}")
            p_t = None
            for a in agents:
                new_order = a.update(p[-a.price_history_len:], info_series[i], fundamental_series[i])
                if new_order is not None:
                    strike_price = order_book.process_order(new_order)
                    if strike_price is not None:
                        p_t = strike_price
                        if new_order.type == 1:
                            fulfilled_buys += 1
                        else:
                            fulfilled_sells += 1

            if order_book.sell_orders:
                sell_price = order_book.sell_orders[0].price
                s.append(sell_price)
            else:
                s.append(s[-1])

            if order_book.buy_orders:
                buy_price = order_book.buy_orders[0].price
                b.append(buy_price)
            else:
                b.append(b[-1])

            if p_t is not None:
                p.append(p_t)
            else:
                p.append(p[-1])

            if order_book.sell_orders and order_book.buy_orders:
                spread.append(sell_price - buy_price)
            else:
                spread.append(np.nan)

            number_of_buys.append(len(order_book.buy_orders))
            number_of_sells.append(len(order_book.sell_orders))
            fulfilled_buys_series.append(fulfilled_buys)
            fulfilled_sells_series.append(fulfilled_sells)

        return MarketData(np.array(p),
                          np.array(b),
                          np.array(s),
                          np.array(number_of_buys),
                          np.array(fulfilled_buys_series),
                          np.array(number_of_sells),
                          np.array(fulfilled_sells_series),
                          np.array(spread)
                          )
