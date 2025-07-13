import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import hindimusic
import englishmusi
import punjabimusic
dfe=pd.read_csv('englishmusic.csv',encoding='ISO-8859-1')
dfp=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')
dfh=pd.read_csv('hindimusic.csv',encoding='ISO-8859-1')
def show():
 st.markdown("""
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #ffcc70;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 100px; /* Set font size to 50px */
    }
    .custom-button:hover {
        background-color: #ff9900;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }
    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #66a5ed;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 60px 80px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 100px; /* Increase font size for larger text */
        width: 300px;
        height: 200px;
    }
    div.stButton > button:first-child:hover {
        background-color: #062447;
        color: white;
        box-shadow: 0 0 15px #86a0bf, 0 0 25px #86a0bf, 0 0 35px #86a0bf;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)
# home
# st.set_page_config(page_title='Gaming')
# st.title(":red[Games]")

# sidebar=st.sidebar.selectbox(label="Select options",options=['Home','Game'])

# if sidebar=='Home':

 
 lang=st.selectbox(label="Choose Language:",options=['English','Hindi','Punjabi'])
 if lang=='Hindi':
  hindimusic.show()
 elif lang=='English':
  englishmusi.show()
 elif lang=='Punjabi':
  punjabimusic.show()
 else:
  st.write("")
