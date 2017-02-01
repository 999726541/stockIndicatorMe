from data_feeder import *
from MA_calculate import *
import pandas as pd


_stock = get_data('GOOG','2016-01-01','2016-06-30')
#print(_stock)
diff = pd.DataFrame(_stock['Adj_Close'].diff())
diff.columns = ['dif']
#print(diff[1:2]['dif']>0)

_stock.loc[:,'Ut'] = 0
_stock.loc[:,'Dt'] = 0
_stock.loc[:,'RS'] = 0
_stock.loc[:,'RSI'] = 0
_stock.loc[:, 'long/short'] = 0

for i in range(1,len(diff)):
    if float(diff[i:i+1]['dif']) >= 0:
        _stock.loc[i:i+1,'Ut'] = float(diff[i:i+1]['dif'])
    else:
        _stock.loc[i:i+1, 'Dt'] = abs(float(diff[i:i + 1]['dif']))
    if i >= 13:
        _stock.loc[i:i + 1, 'RS'] = sma(_stock['Ut'][:i+1],14,i)/sma(_stock['Dt'][:i+1],14,i)
        _stock.loc[i:i + 1, 'RSI'] = 100 - 100/(1 + _stock['RS'][i :i+1])
        if _stock['RSI'][i-1]<20 and _stock['RSI'][i]>20:
            _stock.loc[i:i+1, 'long/short'] = 1
        if _stock['RSI'][i - 1] < 30 and _stock['RSI'][i] > 30:
            _stock.loc[i:i+1, 'long/short'] = 1
_stock.to_html('RSI_GOOG.html')