'''
call, 07/14/2017, $940, $7.50
put, 07/14/2017, $960, $19.50

S_T is the price of the underlying assets at maturity
'''

from matplotlib import pyplot as plt
from pylab import *
import numpy as np

# CALL OPTION
price = np.arange(900, 1000, 1)
strike = 940
premium = 7.5
payoff = [max(-premium, i - strike - premium) for i in price]

plt.plot(price, payoff)
plt.xlabel('Price at T S_T ($)')
plt.ylabel('payoff')
plt.title('Call option Payoff at Expiry')
plt.grid(True)

# PUT OPTION
price = np.arange(900, 1000, 1)
strike = 960
premium = 19.5
payoff = [max(-premium, strike - i - premium) for i in price]

plt.plot(price, payoff)
plt.xlabel('Price at T S_T ($)')
plt.ylabel('payoff')
plt.title('Put option Payoff at Expiry')
plt.grid(True)

plt.show()