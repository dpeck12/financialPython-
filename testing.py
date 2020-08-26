from matplotlib import pyplot as plt
from pylab import *


price = np.arange(900,1000,1)
strike = 940
premium = 7.5
payoff = [max(-premium, i - strike-premium) for i in price]

plt.plot(price, payoff)
plt.xlabel('Price at T S_T ($)')
plt.ylabel('payoff')
plt.title('Call option Payoff at Expiry')
plt.grid(True)

price = np.arange(900,1000,1)
strike = 960
premium = 19.5
payoff = [max(-premium, strike - i -premium) for i in price]

plt.plot(price, payoff)
plt.xlabel('Price at T S_T ($)')
plt.ylabel('payoff')
plt.title('Put option Payoff at Expiry')
plt.grid(True)

plt.show()
