import quandl
import numpy as np 

quandl.ApiConfig.api_key = 'XUgytFMGzRKy9LyXgLz_'

# get quandl data
aapl_table = quandl.get('WIKI/AAPL')

aapl = aapl_table.loc['2017-3',['Open','Close']]

# daily log return 
aapl['log_price'] = np.log(aapl.Close)
aapl['log_return'] = aapl['log_price'].diff()

# calculate monthly return by sum all the daily returns up
month_return = aapl.log_return.sum()

print("Arithmetic Mean: {}".format(np.mean(aapl.log_price)))
print("Variance: {}".format(np.var(aapl.log_price)))
print("Standard Deviation: {}".format(np.std(aapl.log_price)))   