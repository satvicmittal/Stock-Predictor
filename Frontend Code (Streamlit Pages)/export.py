# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:21:05 2021

@author: Meghna and Gayatri
"""

#Fourth Page - Export Data to CSV 

import streamlit as st
import descriptive as ds

#Function for converting dataframe to csv for download option 
def convert_df(stat):
    return stat.to_csv().encode('utf-8')
def app():
    ticker = ''
    st.markdown("<h1 style='text-align: center; ;'>Export Data to CSV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns((1,3,1))
    with col2:
        ticker = st.text_input("Please enter the ticker you want to view the information for:")
        stat = ds.statistics(ticker)
        if ticker != '':
            st.write("Please wait while we download your data")
        
            if stat is None:
                st.warning("Enter a valid ticker")
            else:
                st.dataframe(stat)
                csv = convert_df(stat)
                st.download_button(label='Download', data=csv, file_name = 'StocksData.csv') 
            
            
    
        
           
        
        