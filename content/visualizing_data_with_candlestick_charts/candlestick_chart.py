import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from mpl_finance import candlestick_ohlc

# define time frame

start = dt.datetime(2024, 1, 1)
end = dt.datetime.now()

# get data from Yahoo Finance
df = yf.download('MS', start, end)

print(df.head())
# YF.download() has changed argument auto_adjust default to True
# [*********************100%***********************]  1 of 1 completed
# Price           Close       High        Low       Open   Volume
# Ticker             MS         MS         MS         MS       MS
# Date                                                           
# 2024-01-02  90.001060  90.240680  88.438737  88.812550  6132200
# 2024-01-03  88.093689  89.330119  87.480257  89.330119  7487900
# 2024-01-04  88.323715  89.272606  87.854063  88.323715  8735600
# 2024-01-05  89.368462  90.029814  88.237458  88.381231  6027200
# 2024-01-08  89.627251  89.933963  88.448320  89.339704  6738400

# we need to restructure the data so that only the date and the OHLC data are present
# and the date is in the correct format
# convert the date to a number so that it can be plotted
df = df[['Open', 'High', 'Low', 'Close']]
df.reset_index(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(mdates.date2num)

print(df.head())
# Price      Date       Open       High        Low      Close
# Ticker                  MS         MS         MS         MS
# 0       19724.0  88.812550  90.240680  88.438737  90.001060
# 1       19725.0  89.330119  89.330119  87.480257  88.093689
# 2       19726.0  88.323723  89.272614  87.854071  88.323723
# 3       19727.0  88.381223  90.029806  88.237450  89.368454
# 4       19730.0  89.339704  89.933963  88.448320  89.627251


# Visualization

# the candlestick chart requires a subplot to be created
fig, ax = plt.subplots(figsize=(10, 5))
# set the date format on the x axis
ax.grid(True)
ax.set_axisbelow(True)
ax.xaxis_date()
ax.set_facecolor('black') # optional, by taste
ax.figure.set_facecolor('#121212')
ax.set_title('MSFT Candlestick Chart', color='white')

# setting the tickers/tick parameters to a white color
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
candlestick_ohlc(ax, df.values, width=0.6, colorup='g', colordown='r')
plt.show()