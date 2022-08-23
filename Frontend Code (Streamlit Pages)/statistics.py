# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:43:26 2021

@author: Meghna and Gayatri
"""
#Second Page - Descriptive Analysis

import streamlit as st
import descriptive as ds
st.set_page_config(layout= "wide" )
st.set_option('deprecation.showPyplotGlobalUse', False)


def app():
    ticker=''
    st.markdown("<h1 style='text-align: center; color: black;'>Historical Data Summary \
                </h1>", unsafe_allow_html=True)
    #setting a wider space for column-2 to place widgets in the centre           
    col1, col2, col3 = st.columns((1,3,1)) 
    
    with col2: 
        #Taking ticker input from the user
        ticker = st.text_input("Please enter the ticker you want to view the information \
                               for:")
    try:    
        if ticker != '':
            st.subheader("Descriptive Statistics")
            #Importing function from "descriptive.py" for descriptive stats
            stats = ds.statistics(ticker)
            if stats is None:
                st.warning("Enter a valid ticker")
            else:
                #Using dataframe to display the descriptive table
                st.dataframe(stats)
            
        for i in range(1,3):
            st.text("")
        #Creates a dropdown box with given options.    
        stock_time = st.selectbox(
            "Please select a time-range",
            ('Please select an option','3 Days','5 Days','10 Days','15 Days','1 Month', 
             '2 Months','3 Months','6 Months','9 Months','1 Year','2 Years','3 Years',
             '5 Years', '10 Years', 'Maximum') , index=0)
        
        #Created a dictionary to integrate backend code with GUI 
        dictionary = {"3 Days" : "3d", "5 Days":"5d", "10 Days":"10d", "15 Days": "15d", 
                      "1 Month": "1mo", "2 Months": "2mo", "3 Months": "3mo", 
                      "6 Months": "6mo", "9 Months": "9mo", "1 Year": "1y", "2 Year": "2y",
                      "3 Years": "3y", "5 Years": "5y", "10 Years": "10y", "Maximum": "max"}
        
        #Assigning key list to a variable 
        stock_key = dictionary.keys()
        if stock_time in stock_key:
            time_period = dictionary[stock_time]
        else:
            time_period = ''
        
        stock_type = st.selectbox(
            "Please select a Type of Stock Price",
            ('Please select an option','Open','Close','Low','High','Volume'), index=0)    
        
        graph = st.selectbox(
        "Select the type of graph you would like to see?",
        ('Select an option','ARIMA','Moving Average','Raw-Time Series',
         'Linear Trend Line'), key = "counts" , index=0)
        
        #Defining actions to perform for each graph option
        if graph == 'ARIMA':
            
            #Checking correct stock_type and stock_time for ARIMA
            if(stock_type != 'Volume'):
                if (time_period != '3y' and time_period !='5y' and time_period !='10y' 
                    and time_period !='max'):
                    #Raising a warning for invalid stock_time
                    st.warning("Invalid time-period for ARIMA plot is selected.\
                               Please try again with time-range of 3 Years and above.")
                else:
                    arima_plot= ds.arima(ticker,time_period,stock_type)
                    if arima_plot == 0:
                        st.warning("Enter a valid ticker")
                    elif arima_plot == -1:
                        st.warning("Please select a company which is listed for more than \
                                   3 years for ARIMA")
                    else:
                        st.pyplot(arima_plot)
                        st.write("You are viewing the graph for", graph)
            else:
                #Raising an warning for invalid stock_type
                st.warning("Invalid type of stock price for ARIMA plot, please try again.")
                
        elif graph == 'Moving Average':
            moving_avg = ds.sma(ticker,time_period,stock_type)
            if moving_avg == 0:
                st.warning("Enter a valid ticker")
            else:
                st.pyplot(moving_avg)
                st.write("You are viewing the graph for", graph)
            
        elif graph == 'Raw-Time Series':
            raw_time = ds.raw_trend(ticker,time_period,stock_type)
            if raw_time == 0:
                st.warning("Enter a valid ticker")
            else:
                st.pyplot(raw_time)
                st.write("You are viewing the graph for", graph)
            
        elif graph == 'Linear Trend Line':
            linear_plot= ds.linear_trend(ticker,time_period,stock_type,0)
            if time_period == '' or len(stock_type) > 10:
                st.warning("Select a valid time period")
            else:
                linear_plot= ds.linear_trend(ticker,time_period,stock_type,0)
                if linear_plot == 0:
                            st.warning("Enter a valid ticker")
                else:
                    st.pyplot(linear_plot)
                    st.write("You are viewing the graph for", graph)
        
        else:
             st.write("You have not selected any valid option")
    except:
        st.error('Internal error occured, please refresh the browser and try again.')