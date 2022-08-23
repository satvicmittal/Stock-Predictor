# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:27:14 2021

@author: Meghna and Gayatri
"""

#This is the main page

import streamlit as st

from multipage import MultiPage
#import all the pages in the main app 
from pages import index, statistics, predictor, export, terms, close 


# Create an instance of the app && Default constructor called
stock_predictor = MultiPage()

col1, col2 = st.columns(2)

# Adding all the pages together
stock_predictor.add_page("Please select an option", index.app)
stock_predictor.add_page("Descriptive Analysis", statistics.app)
stock_predictor.add_page("Predict Closing Price", predictor.app)
stock_predictor.add_page("Export Data to CSV", export.app)
stock_predictor.add_page("Terms and Conditions", terms.app)
stock_predictor.add_page("Exit", close.app)

# The main app runs from here
stock_predictor.run()