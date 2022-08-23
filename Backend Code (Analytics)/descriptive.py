import warnings
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import matplotlib
import yfinance as yf
import time
from predictive import predictor
from matplotlib.pylab import rcParams
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
rcParams['figure.figsize'] = 20,10
rcParams.update({'axes.facecolor':'seashell'})
warnings.filterwarnings("ignore")

def input_data(ticker, period = 'max'):
    # Fetching the data by hitting the Yahoo finance API
    stock = yf.Ticker(ticker) 
    stock = stock.history(period = period)
    time.sleep(1)
    return stock
    
def hypertune(y):
    # Creating a list of values for p,d,q for doing a grid search
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

    i = 100000000
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y, order = param,seasonal_order = param_seasonal,
                                                enforce_stationarity=False, enforce_invertibility=False) 
                results = mod.fit()
                ''' selecting the values of p,d,q for the lowest value of AIC(the lower the better)
                Akaike information criterion '''
                if results.aic < i:
                    i = results.aic
                    j = param
                    k = param_seasonal
            except:
                continue
    return j,k



def plot(y,results):  
    # Plotting the ARIMA graph
    pred = results.get_prediction(start=pd.to_datetime('2019-01-01'), dynamic=False)
    ax = y['2019':].plot(label='Observed') #check for start date of the stock
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.9)
    ax.set_xlabel('TIME',fontsize = 20)
    ax.set_ylabel('STOCK PRICE',fontsize = 20)
    plt.title('ARIMA', fontsize = 30)
    plt.legend(fontsize = 15, loc= 'best').get_frame().set_edgecolor('k')
    plt.show()
    
    
    
def arima(ticker,period,price):
    '''This funtion returns the ARIMA plot, for incorrect ticker 0 is returned,
    and for any other processing error -1 is returned. This can further be used for 
    error handling''' 
    stock = input_data(ticker,period)
    if len(stock) > 0:
        type_price = stock[price] 

        """ 
        Resampling the datetime data. Here we use the start of each month as the
        timestamp and take the average daily sales value for a particular month 
        since working with the current datetime data becomes tricky.
        'MS' stands for month start which samples data on the basis of the starting 
        of the month
        """
        y = type_price.resample('MS').mean()
        
        try:
            '''parameter finalising for ARIMA (p, d, q -- p- autoregressive lags, q- moving average order, 
              d - lags used to make the series stationary)''' 
            j,k = hypertune(y)
        
            # Time Series Forecasting using ARIMA
            mod = sm.tsa.statespace.SARIMAX(y,order=j,seasonal_order=k)
            results = mod.fit()
            
            # Plotting ARIMA
            arima_plot = plot(type_price,results)
            return arima_plot
        except:
            return -1
    else:
        return 0
        
    
    
def raw_trend(ticker,period,price):
     # Prints the raw trend line
     stock = input_data(ticker,period) 
     if len(stock) > 0:
         # Historical time series
         type_price = stock[price] 
         type_price['2002':].plot(figsize=(20,10))
         plt.xlabel('TIME')
         plt.ylabel('STOCK PRICE')
         plt.title('HISTORICAL DATA', fontsize = 30)
         raw_plot = plt.show()
         return raw_plot
     else:
         return 0



def linear_trend(ticker,period,price,flag): 
    # Importing file predictive to call method predictor
    linear_plot = predictor(ticker,period,price,flag)
    return linear_plot   
    
    
    
def statistics(ticker):
    # Displaying the descriptive statistics 
    stock = input_data(ticker)
    if len(stock) > 0:
        pd.set_option('display.max_columns', None)
        stats = stock.describe()
        return stats
    else:
        return None
    
    
    
def sma(ticker,period,price):
    # Simple Moving Average
    stock = input_data(ticker,period)
    if len(stock) > 0:
        # Calculating 4 days simple moving average
        stock['rolling_mean4'] = stock[price].rolling(window=4).mean()
        
        x = pd.to_datetime(stock.index, unit='D')
        
        #ploting the SMA
        plt.plot(x,stock[price], label='Price History', color = 'coral')
        plt.plot(x,stock['rolling_mean4'], color='darkblue', label='Moving Average')
        plt.xlabel('TIME', fontsize = 20)
        plt.ylabel('STOCK PRICE', fontsize = 20)
        plt.title('SIMPLE MOVING AVERAGE', fontsize = 30)
        plt.legend(fontsize = 15, loc= 'best').get_frame().set_edgecolor('k')
        sma_plot = plt.show()
        return sma_plot
    else:
        return 0
