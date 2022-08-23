# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:25:03 2021

@author: Meghna and Gayatri
"""

#Third Page - Predict Closing Price

import streamlit as st
import predictive as pd

def app():
    ticker=''
    timer=''
    st.markdown("<h1 style='text-align: center; color: black;'>Predict Closing Price \
                </h1>", unsafe_allow_html=True)
    #Added columns to position widegets on the UI            
    col1, col2, col3 = st.columns((1,3,1))  
    with col2:
    
        for i in range (1,3):
            st.text("")
        #Input ticker value taken by the user    
        ticker = st.text_input("Please enter the ticker you want prediction for:")  
        #Set default value as close as closing price is being predicted
        price= 'Close'  
        
        #Modelling period input taken by the user
        modellingPeriod = st.selectbox( 
        "Select a modelling period",
        ('Please select an option','1 Month','2 Months','3 Months','6 Months','9 Months','1 Year',
         '2 Years','5 Years','10 Years','Maximum' ), index = 0)
        
        #Dictionary is created so that user enter the value as "! month" and the value is sent to the alogrithm as '1mo'
        modellingPeriodDict= {"1 Month": "1mo", "2 Months": "2mo","3 Months": "3mo", "6 Months": "6mo", "9 Months": "9mo", 
                              "1 Year": "1y", "2 Years": "2y","5 Years": "5y",
                              "10 Years": "10y","Maximum": "max"}  
        modellingPeriodKeys = list(modellingPeriodDict.keys())
        
        if modellingPeriod in modellingPeriodKeys:  
            timer = modellingPeriodDict[modellingPeriod]
        
        #Number of days been taken as an input via a slider
        days = st.slider(
        'For how many days do you want to predict the data',
        min_value=1, max_value=365, key = "hit", step=1)
        if ticker !='':
            if len(price) <= 10:                #Condition added to check the field value has been selected and not a default value
                if len(modellingPeriod) <= 10:  #Condition added to check the field value has been selected and not a default value
                    if days !='':
                        y_predict,r2,rmse,graph= pd.predictor(ticker,timer,price,1,days)
                        if y_predict == 0:
                            st.warning("Please enter a valid ticker")
                        else:
                            st.pyplot(graph)
                            st.write("Closing price at the {}th day would be around = {} ".format(days,y_predict))
                            st.write("The coefficient of determination (R^2) is {}.".format(round(r2,3)))
                            st.write("The root mean square error is {}.".format(round(rmse,3)))
                    else:
                        st.warning('Select Days')
                else:
                    st.warning('Select Time Range')
            else:
                st.warning('Select Price Type')
        else:
            st.warning('Select stock')