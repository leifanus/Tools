from find_data import *
import time
import pandas as pd
import numpy as np

startDate = [2017, 12, 29]
endDate = [2017, 12, 29]


startDate2 = [2017, 1, 1]
endDate2 = [2017, 12, 29]

tickers = pd.read_csv('nasdaq2WRDS.txt', header = None)
tickers_list = []
tickers = np.array(tickers)

for i in range(len(tickers)):
	tickers_list.append(str(tickers[i][0]))

# print(tickers_list)
ticker_final = []
price = []
divid = []
divid_rate = []
date_list = []
for i in range(len(tickers_list)):
	try:
		stock = getData(tickers_list[i], startDate, endDate)
		stock2 = getData(tickers_list[i], startDate2, endDate2)
		Closeprice = stock.Closeprice()
		ticker_final.append(tickers_list[i])
		price.append(Closeprice[0])
		dividends = sum(np.array(stock2.Dividends()))
		print(i, tickers_list[i], dividends)
		divid.append(dividends)
		divid_rate.append(dividends/float(Closeprice[0]))
		date_list.append('2017-12-29')
		print(len(ticker_final), len(price), len(date_list), len(divid), len(divid_rate))
		result = pd.DataFrame({'Tickers':ticker_final, 'ClosePrice': price, 'Date': date_list, 'Annual Dividends': divid, 'Dividend rate': divid_rate})
		result.to_csv('price.csv')
		if len(ticker_final)!= len(date_list):
			print(len(tickers_final), len(date_list))
			print(tickers_list[i], Closeprice, dividends)
			break
	except:
		print('Error: ', tickers_list[i])

# print(len(ticker_final), len(price), len(date_list), len(divid), len(divid_rate))
# result = pd.DataFrame({'Tickers':ticker_final, 'ClosePrice': price, 'Date': date_list, 'Annual Dividends': divid, 'Dividend rate': divid_rate})
# result.to_csv('price.csv')