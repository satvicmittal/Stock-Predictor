# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:16:02 2021

@author: Meghna and Gayatri
"""

#Fifth Page - Terms & Conditions

import streamlit as st
from PIL import Image

def app():
    #Inserting an image as a part of terms and conditions 
    image = Image.open('C:\\Users\\meghn\\Desktop\\StockPredictor_GUI\\pages\\t&c.jpg')
    st.image(image, caption='Terms and conditions applied')
    