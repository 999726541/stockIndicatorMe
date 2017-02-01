from data_feeder import *
from MA_calculate import *
import pandas as pd


_stock = get_data('GOOG','2016-01-01','2016-06-30')
#_stock.to_csv('AAPLL.csv')

def find_KD(_stock,n,dn):
    stock = _stock
    stock.loc[:,'K_indicator'] = 0
    stock.loc[:,'D_indicator'] = 0
    stock.loc[:, 'long/short'] = 0
    for i in range(n,len(stock)+1):
        stock.loc[i-1:i,'K_indicator'] = 100 * (float((stock['Adj_Close'][i-1:i]))-min(list(stock['Low'][i-n:i])))/(
            max(list(stock['High'][i - n:i]))-min(list(stock['Low'][i - n:i])))
        #print(min(list(stock['Low'][i-n:i])),max(list(stock['High'][i - n:i])))
        if i >= n+dn-1:
            stock.loc[i - 1:i, 'D_indicator'] = sma(list(stock['K_indicator'][:i]),dn,i-1)

        if stock['K_indicator'][i - 2] < stock['D_indicator'][i - 2] and \
                        stock['K_indicator'][i - 1] >= stock['D_indicator'][i - 1]:
            stock.loc[i - 1:i, 'long/short'] = 1

    return stock

find_KD(_stock,10,3).to_html('KD.html')