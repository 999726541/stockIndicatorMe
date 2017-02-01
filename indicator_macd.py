from data_feeder import *
from MA_calculate import *
import pandas as pd


_stock = get_data('GOOG','2016-01-01','2016-06-30')
#_stock.to_csv('AAPLL.csv')
stock_12 = find_ema(_stock,12,'Adj_Close')
stock_26 = find_ema(_stock,26,'Adj_Close')
stock = pd.concat([stock_12,stock_26],axis=1).dropna()
print(stock)
macd = stock.ema_12_Adj_Close-stock.ema_26_Adj_Close
macd.name = 'macd'
stock = pd.concat([stock,macd],axis=1)
stock = find_ema(stock,9,'macd')
signal = stock.macd - stock.ema_9_macd
diff = stock.macd - stock.ema_9_macd
diff.name = 'sig_diff'
signal.name = 'sig'
signal = pd.DataFrame(signal)

signal.loc[signal['sig'] > 0,'sig'] = 1
signal.loc[signal['sig'] <= 0,'sig'] = 0

aa = signal.diff()
aa.loc[aa['sig'] <= 0,'sig'] = 0
signal = pd.concat([stock,aa,diff],axis = 1)
signal.to_html('MACD_12_26.html')

