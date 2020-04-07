
import yFinance as yf
data = yf.download(tickers='MSFT', period = '5d', interval = '1m')
data.head()

#KeyRatios
msft=yf.Ticker('MSFT')
pb = msft.info['priceToBook']
pe = msft.info['regularMarketPrice']/msft.info['epsTrailingTwelveMonths']
print('Price to Book Ratio is: %.2f' % pb)
print('Price to Earnings Ratio is: %2f' % pe)

#Revenues
import matplotlib.pyplot as plt

revenue = msft.financials.loc['Total Revenue']
plt.bar(revenue.index, revenue.values)
plt.ylabel('Total Revenue')
plt.show()

#Earnings Before Interest and Taxes
EBIT = msft.financials.loc['Earnings Before Interest and Texes']
plt.bar(EBIT.index, EBIT.value)
plt.ylabel('EBIT')
plt.show()

#BalanceSheetandCashFlow
msft.financials
msft.balance_sheet
msft.cashflow
msft.info


