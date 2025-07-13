import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import hindimovie
import englishmovie
import punjabimovie
st.markdown("""
    <style>
    /* Neon-style Streamlit button styling */
    div.stButton > button:first-child {
        background-color:#0f0f0f;
        color:#2653d1;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        border: 2px solid #2653d1;
        border-radius: 15px;
        padding: 20px 30px;
        font-size: 100px;
        width: 200px;
        height: 50px;
        text-shadow: 0 0 5px #2653d1, 0 0 10px #2653d1;
        box-shadow: 0 0 10px #2653d1, 0 0 20px #2653d1, 0 0 30px #2653d1;
        transition: 0.3s ease-in-out;
    }

    div.stButton > button:first-child:hover {
        background-color: #1f1f1f;
        color: #00ffff;
        border-color: #00ffff;
        text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
        box-shadow: 0 0 15px #00ffff, 0 0 25px #00ffff, 0 0 35px #00ffff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)
dfe=pd.read_csv('engmov.csv',encoding='ISO-8859-1')
# dfp=pd.read_csv('punjabimov.csv',encoding='ISO-8859-1')
dfh=pd.read_csv('hindimov.csv',encoding='ISO-8859-1')
dfp=pd.read_csv('punjmov.csv',encoding='ISO-8859-1')
# sidebar=st.sidebar.selectbox(label="Select options",options=['Home','Game'])

# if sidebar=='Home':
def show():
 
 lang=st.selectbox(label="Choose Language:",options=['English','Hindi','Punjabi'])
 if lang=='Hindi':
  hindimovie.show()
 elif lang=='English':
  englishmovie.show()
 elif lang=='Punjabi':
  punjabimovie.show()
 else:
  st.write("")
# show()