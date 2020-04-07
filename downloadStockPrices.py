import pandas as pd
import yFinance as yf


teslaD = yf.download('TSA', start = '2020-01-01', end = '2020-03-03', progress = 'False')
teslaD.head()

#msft = yf.Ticker('MSFT', start= '2020-01-01', end = '2020-03-03')
ticker = yf.Ticker('TSLA')
tesla = ticker.history(period='max')
tesla['Close'].plot(title='Tesla\'s stock price: ' )

tesla.info()
tesla.major_holders()





