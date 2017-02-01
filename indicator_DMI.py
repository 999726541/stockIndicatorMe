from data_feeder import *
from MA_calculate import *
import pandas as pd


_stock = get_data('GOOG','2016-01-01','2016-06-30')
#_stock.to_csv('AAPLL.csv')

def find_DM(_stock):
    stock = _stock
    stock.loc[:,'Up_move'] = 0
    stock.loc[:,'Down_move'] = 0
    for i in range(1,len(stock)):
        upDM = stock['High'][i:i+1] - stock['High'][i-1:i]
        dowDM = stock['Low'][i-1:i] - stock['Low'][i:i+1]
        if upDM > 0 or dowDM >0:
            if upDM > dowDM:
                stock.loc[i:i+1, 'Up_move'] = upDM
            if dowDM > upDM:
                stock.loc[i:i + 1, 'Down_move'] = dowDM
    return stock

def find_TR(_stock,n):
    stock = _stock
    stock.loc[:, 'TR'] = 0
    stock.loc[:, 'ATR'] = 0
    for i in range(1,len(_stock)):
        stock.loc[i:i + 1, 'TR'] = max([stock['High'][i] - stock['low'][i],stock['High'][i] - stock['Close'][i-1],stock['Low'][i] - stock['Close'][i-1]])
        if i >= n-1:
            stock.loc[i:i + 1, 'ATR'] = 0