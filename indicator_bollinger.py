from data_feeder import *
from MA_calculate import *
import pandas as pd
import numpy as np
from IPython.display import display, HTML

_stock = get_data('GOOG','2016-01-01','2016-06-30')
#_stock.to_csv('AAPLL.csv')
def find_bollinger(_stock,n,a):
    stock = _stock
    stock.loc[:,'upper'] = 0
    stock.loc[:,'lower'] = 0
    stock.loc[:, 'mean'] = 0
    stock.loc[:,'std'] = 0
    stock.loc[:, 'long/short'] = 0
    for i in range(n,len(stock)+1):
        price_list = list(stock['Adj_Close'][:i])
        #print(price_list)
        _ma = sma(price_list,n,len(price_list)-1)
        stock.loc[i-1:i, 'mean'] = _ma
        stock.loc[i-1:i, 'std'] = std(price_list,n,len(price_list)-1)
        stock.loc[i-1:i,'upper'] = _ma + a*std(price_list,n,len(price_list)-1)
        stock.loc[i-1:i, 'lower'] = _ma - a * std(price_list, n, len(price_list) - 1)
        if stock['Adj_Close'][i-1] < stock['lower'][i-1]:
            stock.loc[i-1:i, 'long/short'] = 1
        if stock['Adj_Close'][i-1] > stock['upper'][i-1]:
            stock.loc[i - 1:i, 'long/short'] = -1
    return stock

find_bollinger(_stock,10,1.5).to_html('ei.html')

