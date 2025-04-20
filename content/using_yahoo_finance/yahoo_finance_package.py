# resource: youtube.com/watch?v=t_vZDyQDUkk

import datetime as dt
#import pandas_datareader as web            # deprecated
#from pandas_datareader import data as pdr  # deprecated
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# define time frame
start = dt.datetime(2024, 1, 1)
end = dt.datetime.now()

# all these pandas-datareader functions are deprecated:
# df = web.DataReader('GOOG', 'yahoo', start, end)
# df = web.yahoo.daily.YahooDailyReader('GOOG', start, end)
# df = pdr.get_data_yahoo('GOOG', start, end)

# get data from Yahoo Finance
df = yf.download('MS', start, end)
print(df.head())
# YF.download() has changed argument auto_adjust default to True
# [*********************100%***********************]  1 of 1 completed
# Price           Close       High        Low       Open   Volume
# Ticker             MS         MS         MS         MS       MS
# Date                                                           
# 2024-01-02  90.001060  90.240680  88.438737  88.812550  6132200
# 2024-01-03  88.093697  89.330126  87.480264  89.330126  7487900
# 2024-01-04  88.323715  89.272606  87.854063  88.323715  8735600
# 2024-01-05  89.368469  90.029821  88.237465  88.381238  6027200
# 2024-01-08  89.627251  89.933963  88.448320  89.339704  6738400

# the dataframe's index will be a datetime index

print(df.columns)
# MultiIndex([( 'Close', 'MS'),
#             (  'High', 'MS'),
#             (   'Low', 'MS'),
#             (  'Open', 'MS'),
#             ('Volume', 'MS')],
#            names=['Price', 'Ticker'])

# accessing different columns in the dataframe

close = df['Close']
print(close.head())
# Ticker             MS
# Date                 
# 2024-01-02  90.001060
# 2024-01-03  88.093681
# 2024-01-04  88.323708
# 2024-01-05  89.368454
# 2024-01-08  89.627251

# workign with multiple tickers' data:
multiple_df = yf.download(['MS', 'GOOG', 'SBUX'], start, end)
print(multiple_df.head())
print(multiple_df['Close'].head())
# [*********************100%***********************]  3 of 3 completed
# Price            Close                              High  ...       Open    Volume                  
# Ticker            GOOG         MS       SBUX        GOOG  ...       SBUX      GOOG       MS     SBUX
# Date                                                      ...                                       
# 2024-01-02  138.902084  90.001060  90.796104  139.952119  ...  92.521491  20071900  6132200  8859700
# 2024-01-03  139.698334  88.093689  90.369621  140.424888  ...  91.077220  18974300  7487900  7161700
# 2024-01-04  137.389252  88.323715  90.679802  139.972020  ...  90.243604  18253300  8735600  7118600
# 2024-01-05  136.742325  89.368462  90.136971  138.155629  ...  90.466543  15433200  6027200  7189900
# 2024-01-08  139.867508  89.627258  91.300163  139.976990  ...  90.166054  17645300  6738400  7536900

# [5 rows x 15 columns]
# Ticker            GOOG         MS       SBUX
# Date                                        
# 2024-01-02  138.902084  90.001060  90.796104
# 2024-01-03  139.698334  88.093689  90.369621
# 2024-01-04  137.389252  88.323715  90.679802
# 2024-01-05  136.742325  89.368462  90.136971
# 2024-01-08  139.867508  89.627258  91.300163

# looking at the last _100 calendar_ days of data (notice that it's 67 trading days):
m_close = multiple_df['Close']
print(m_close[m_close.index > end - dt.timedelta(days=100)].describe(percentiles = [0.1, 0.5, 0.9]))
# Ticker        GOOG          MS        SBUX
# count    67.000000   67.000000   67.000000
# mean    176.583256  124.909635  100.773787
# std      16.583312   11.932311   10.307011
# min     146.580002   99.830002   79.690002
# 10%     155.835999  108.714001   85.098000
# 50%     174.011765  124.269997   99.190002
# 90%     199.372867  138.629993  113.012000
# max     207.473633  141.080002  115.809998

# m_close.plot() would work in a jupyter notebook
# ...or better yet, plotly
