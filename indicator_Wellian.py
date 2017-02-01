from data_feeder import *
from MA_calculate import *
import pandas as pd


_stock = get_data('GOOG','2016-01-01','2016-06-30')
#_stock.to_csv('AAPLL.csv')

def find_William(_stock,n):
    stock = _stock
    stock.loc[:,'Hn'] = 0
    stock.loc[:,'Ln'] = 0
    stock.loc[:, '%R'] = 0
    _stock.loc[:, 'long/short'] = 0
    for i in range(n,len(stock)+1):
        stock.loc[i - 1:i,'Hn'] = max(list(stock['High'][i-n:i]))
        stock.loc[i - 1:i, 'Ln'] = min(list(stock['Low'][i-n:i]))
        stock.loc[i - 1:i, '%R'] = -100*(stock['Hn'][i-1]-stock['Adj_Close'][i-1])/(stock['Hn'][i-1]-stock['Ln'][i-1])
        if _stock['%R'][i - 2] < -20 and _stock['%R'][i-1] > -20:
            _stock.loc[i-1:i, 'long/short'] = 1
        if _stock['%R'][i - 2] < -80 and _stock['%R'][i-1] > -80:
            _stock.loc[i-1:i, 'long/short'] = 1
    return stock
find_William(_stock,10).to_html('William_.html')