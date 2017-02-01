import pandas as pd

def match(df1,df2,df3):
    result = pd.concat([df1, df2, df3], axis=1, join_axes=[df1.index])
    result = result.dropna()
    return result

if __name__=='__main__':
    df1 = pd.read_excel('/Users/leotao/Downloads/e-min.xlsx',names=['date','close','open','4','5','6','7'])
    df1.date = df1.date.astype(str)
    df1 = df1.set_index('date')
    df1 = pd.DataFrame(df1.close)
    df1.columns = ['e-min']
    print(df1.index)

    df2 = pd.read_csv('/Users/leotao/Downloads/CHRIS-CBOE_VX2.csv')
    df2 = df2.set_index('date')
    df2 = pd.DataFrame(pd.concat([df2.Close,df2.Open],axis=1))
    df2.columns = ['vix2close','vix2open']
    print(df2.index)

    df3 = pd.read_csv('/Users/leotao/Downloads/CHRIS-CBOE_VX1.csv')
    df3 = df3.set_index('date')
    df3 = pd.DataFrame(pd.concat([df3.Close,df3.Open],axis=1))
    df3.columns = ['vix1close','vix1open']
    print(df3.index)

    zz = match(df1, df2, df3)
    zz.to_csv('/Users/leotao/Downloads/research.csv')
    print(zz)