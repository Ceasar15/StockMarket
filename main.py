import pandas as pd
from pandas_datareader import data

start_date = '2019-01-01'
end_date = '2020-01-01'
ticker = 'AMZN'

data = data.get_data_yahoo(ticker, start_date, end_date)
data.head()

import matplotlib.pyplot as plt
from matplotlib import inline
from astropy.utils.tests import data
data['Adj Close'].plot(figsize=(10,7))
plt.title('Adjusted Close Price of %s' % ticker, fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which='major', color='k', linestyle='_.', linewidth=0.5)
plt.show()


