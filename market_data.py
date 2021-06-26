from collections import namedtuple

MarketData = namedtuple("MarketData",
                        [
                            "prices",
                            "buy_price",
                            "sell_price",
                            "buy_orders_num",
                            "fulfilled_buy_orders",
                            "sell_orders_num",
                            "fulfilled_sell_orders",
                            "spread"
                        ])