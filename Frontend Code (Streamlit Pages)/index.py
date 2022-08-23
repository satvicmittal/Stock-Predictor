# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:01:52 2021

@author: Meghna
"""

#First Page - Welcome page

import streamlit as st

def app():
    #Using Markdown to implement HTML style formatting in streamlit
    st.markdown("<h1 style='text-align: center; color: black;'> <u> WELCOME TO STOCK PREDICTIONS </u> </h1>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 style='text-align: center; color: black;'>Please use the sidebar navigation to get an insight on your chosen stocks</h3>", unsafe_allow_html=True)
    st.write("")
    for i in range (1,3):
            st.text("")
    st.markdown("<h4 style='text-align: center; color: black;'>You can find the following information about your stocks in this predictor:</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns((1,1,1))
    with col2:
        for i in range (1,3):
            st.text("")
        st.markdown("<h5 color: black;'>1. Historical Data Summary</h5>", unsafe_allow_html=True)    
        st.markdown("<h5 color: black;'>2. Predict Stock Prices</h5>", unsafe_allow_html=True)    
        st.markdown("<h5 color: black;'>3. Download the Stock File</h5>", unsafe_allow_html=True)    
            
        