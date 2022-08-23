import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from matplotlib.pylab import rcParams

import yfinance as yf
import time

def accuracy (y,y_learned):
    '''Calculates the rmse for the model which gives us the erorr difference 
      between predicted and actual value (or residual).'''
    rmse = sqrt(mean_squared_error(y, y_learned))

    '''r2 for the model
    Gives the proportion of variation of y that could be explained by the 
    regression model'''
    r2 = r2_score(y, y_learned)
    r2 = round(r2, 3)
    
    return rmse,r2
    

    
def predictor(ticker,period='max',price = 'Close',flag = True,step = 10):
    '''returns the prediction value, r2, rmse, graph at nth day when flag is set true (predictive)
     else return only the graph when flag is set to false (descriptive)
     If the user enters an invalid ticker then it returns 0
     fetch the data by hitting the API'''
    stock = yf.Ticker(ticker) 
    stock = stock.history(period = period)
    time.sleep(1)
    if len(stock) > 0:
        '''As dates cannot be passed directly to a regression model
          we convert the dates into number of days'''
        date = stock.index[0].strftime('%Y-%m-%d')
        stock.index = (stock.index - pd.to_datetime(date)).days
        
        '''Converting the pandas series into numpy array as we will require 
        them to pass them into the regression model.
        y is the dependent variable and x is the independent variable'''
        y = np.asarray(stock[price])
        x = np.asarray(stock.index.values)
        
        '''Model initialization
          This generates a mathematical model for an equation of line which is 
          y = mx + c'''
        regression_model = LinearRegression()
    
        # Fit the data(train the model)
        regression_model.fit(x.reshape(-1, 1), y.reshape(-1, 1))
    
        '''Prediction for historical dates to further estimate the accuracy of the model
          It is named as y_learned'''
        y_learned = regression_model.predict(x.reshape(-1, 1))
        
        # Estimation of accuracy for the model
        if flag:
            rmse,r2 = accuracy(y,y_learned)
        
        '''Adding future dates to the date index and passing the same to the 
        regression model for future prediction. '''
        newindex = np.asarray(pd.RangeIndex(start=x[-1], stop=x[-1] + step))
    
        # Future Prediction. It is named as y_predict.
        y_predict = regression_model.predict(newindex.reshape(-1, 1))
        
        #converting the days index back to dates index for plotting the graph
        x = pd.to_datetime(stock.index, origin= date, unit='D')
        x_future = pd.to_datetime(newindex, origin= date, unit='D')
        
        graph = plot(x,y,y_learned,y_predict,x_future,flag)
        
        if flag:
            return y_predict[-1],r2,rmse,graph
        else:
            return graph
    else:
        # Returning 0 if invalid ticker is entered by the user
        if flag:
            return 0,0,0,0
        else:
            return 0
    
    
def plot(x,y,y_learned,y_predict,x_future,flag):
    #setting figure size
    rcParams['figure.figsize'] = 20,10
    rcParams.update({'axes.facecolor':'seashell'})

    #plot the actual data
    #plt.figure(figsize=(20,10))
    plt.plot(x,y, label='Historical Price')

    #plot the regression model
    plt.plot(x,y_learned, color='r', label='Linear line')

    #plot the future predictions
    if flag:
        plt.plot(x_future,y_predict, color='g', label='Future predictions')
    
    if flag:
        plt.title('STOCK MARKET PREDICTIONS', fontsize = 30)
    else:
        plt.title('LINEAR TREND LINE', fontsize = 30)
        
    plt.xlabel('TIME',fontsize = 20)
    plt.ylabel('CLOSING PRICE',fontsize = 20)
    plt.legend(fontsize = 15, loc= 'best').get_frame().set_edgecolor('k')
    plot = plt.show()
    
    return plot

