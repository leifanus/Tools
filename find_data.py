#!/usr/bin/python

#Filename: find_data.py

import pandas as pd
import datetime
import pandas_datareader.data as web
import numpy as np

class getData:

	def __init__(self , name , startDate , endDate):

		self.name = name

		self.startDate = startDate

		self.endDate = endDate

	#Get close price during specific time

	def Closeprice(self):

		start = datetime.datetime(self.startDate[0],self.startDate[1],self.startDate[2])

		end = datetime.datetime(self.endDate[0],self.endDate[1],self.endDate[2])

		D = web.DataReader(self.name , "yahoo", start , end)

		return D[:]["Close"]
		# return D[:]
	def Dividends(self):

		start = datetime.datetime(self.startDate[0],self.startDate[1],self.startDate[2])

		end = datetime.datetime(self.endDate[0],self.endDate[1],self.endDate[2])

		D = web.DataReader(self.name , "yahoo-dividends", start , end)

		return D[:]["value"]





# import pandas as pd
# import datetime
# import pandas_datareader.data as web
# import numpy as np

# class getData:

# 	def __init__(self , name , startDate , endDate):

# 		self.name = name

# 		self.startDate = startDate

# 		self.endDate = endDate

# 	#Get close price during specific time

# 	def Closeprice(self):

# 		start = datetime.datetime(self.startDate[0],self.startDate[1],self.startDate[2])

# 		end = datetime.datetime(self.endDate[0],self.endDate[1],self.endDate[2])

# 		D = web.DataReader(self.name , "yahoo-dividends", start , end)

# 		# return D[:]["Close"]
# 		return D[:]