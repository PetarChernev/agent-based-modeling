import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from agent import NoiseAgent, Agent
from market import Market


max_t = 1000
n_agents = 100
info_var_squared = 1
fundamental_change_var_squared = 1
s_0 = 100
sentiment_dist = stats.norm(0, 0.5)
reaction_strength_dist = stats.norm(0.5, 0.5)

agents = [
    NoiseAgent(
        shares=100000,
        capital=10000000,
        sentiment=sentiment_dist.rvs(),
        reaction_strength=1,
        order_period=0.8,
        info_var_squared=info_var_squared,
        price_history_len=0
    )
    for i in range(n_agents)]
market = Market(info_var_squared, fundamental_change_var_squared)

market_data = market.simulate(agents, max_t, s_0)

returns = (market_data.prices / np.roll(market_data.prices, 1))[1:]
print(len(returns[returns==1])/len(returns))

fig, axs = plt.subplots(2, 1)
axs[0].plot(market_data.prices)
axs[1].plot(market_data.buy_orders_num, label="unfulfilled buy orders", c='g')
axs[1].plot(market_data.sell_orders_num, label="unfulfilled sell orders", c='r')
axs[1].legend()

print(np.mean(Agent.personal_infos))
print(np.mean(market_data.buy_orders_num - market_data.sell_orders_num))
plt.show()
