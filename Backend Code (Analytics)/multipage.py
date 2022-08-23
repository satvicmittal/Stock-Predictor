# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:24:34 2021

@author: Meghna and Gayatri
"""

import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    #Creating a framework for adding multiple pages together

    def __init__(self) -> None:
        #Constructor class to generate a list which will store all our applications as an instance variable.
        self.pages = []
        
    #Function to add pages with title and all functionalities
    def add_page(self, title, func) -> None: 
        self.pages.append({
                "title": title, 
                "function": func
            })

    def run(self):
        #Implementing sidebar to show the page navigation  
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, key = "title",
            format_func=lambda page: page['title']
        )

        # Run the GUI function from stock_predictor
        page['function']()