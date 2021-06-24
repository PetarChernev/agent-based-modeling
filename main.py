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
sentiment_dist = stats.norm(0, 2)

agents = [NoiseAgent(sentiment_dist.rvs(),
                     5 * np.random.random(),
                     3 * np.random.random(),
                     info_var_squared,
                     10)
          for _ in range(n_agents)]
market = Market(info_var_squared, fundamental_change_var_squared)

market_data = market.simulate(agents, max_t, s_0)

returns = (market_data.prices / np.roll(market_data.prices, 1))[1:]
print(len(returns[returns==1])/len(returns))

for name, data in market_data._asdict().items():
    if name in ['buy_price', 'sell_price']:
        continue
    plt.plot(data, label=name)
plt.legend()
# print(stats.normaltest(returns))
# plt.hist(returns, bins=100)
# plt.plot(np.linspace(0.99, 1.01, 100), 20000*stats.norm(1, np.var(returns)).pdf(np.linspace(-10, 10, 100)))
print(np.mean(Agent.personal_infos))
print(np.mean(market_data.buy_orders_num - market_data.sell_orders_num))
plt.show()
