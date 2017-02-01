import pandas as pd


def find_ema(df,n,name):
    if len(df) < n: raise str('No enough data to calculate MA')
    # df = pd.rolling_mean(self.__df['close'], n)
    i, ma = ema([],list(df[name]),n,len(df[name])-1)
    # print(len(ma),len(df))
    df = df[n-1:]

    name = 'ema_' + str(n) +'_' +name
    ma = pd.DataFrame({name:ma,'Date':list(df.index)})
    ma.set_index('Date',inplace=1)
    df = pd.concat([df, ma], axis=1)
    print('calculated: ' + name + ' success')
    return df




def ema(_ema,_close,_n,_t):
    m = 2/(_n+1)
    if _t>=_n:
        e0,_ema = ema([],_close,_n,_t-1)
#         print("(",close[_t],"-",e0,")*",m,"+",e0)
        e = (_close[_t] - e0)*m + e0
        _ema.append(e)
        return e,_ema
    else:
        s = sma(_close,_n,_t)
#         print(s)
        _ema.append(s)
        return s,_ema


def sma(_close,_n,_t):
    return sum(_close[_t-_n+1:_t+1])/_n

def std(_close,_n,_t):
    _ma = sma(_close,_n,_t)
    #print(_ma)
    #print([(i-_ma)**2 for i in _close[_t-_n+1:_t+1]])
    return ((sum([(i-_ma)**2 for i in _close[_t-_n+1:_t+1]]))/(_n-1))**0.5

if __name__ =='__main__':
    i = [0,2,3,5,6,6,6]
    print(sma(i,3,len(i)))