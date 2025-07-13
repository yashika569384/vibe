import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import urllib     
import music
import movie
import kdrama       
import englishmusic
import hindimusic
import hindimovie
import punjabimovie
import punjabimusic

# st.set_page_config(page_title='VibeVista')
st.title(":red[Welcome :microphone:]")
dfk=pd.read_csv('kdrama1 final.csv',encoding='ISO-8859-1')
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
df1=pd.read_csv('englishmusic.csv',encoding='ISO-8859-1')
df2=pd.read_csv('hindimusic.csv',encoding='ISO-8859-1')
df3=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')


# st.set_page_config(page_title="Music Selector", layout="wide")

def show():
#  st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(45deg, #ff7eff, #ff4d99, #8e44ad, #3498db, #f39c12);
#         background-size: 400% 400%;
#         animation: gradientAnimation 10s ease infinite;
#         color: white;
#         font-family: 'Courier New', Courier, monospace;
#     }

#     @keyframes gradientAnimation {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }

#     /* Glow effect for text */
#     h1, h2, h3, p {
#         text-shadow: 0 0 15px #ff7eff, 0 0 30px #ff7eff, 0 0 45px #ff7eff;
#     }
#     </style>
# """, unsafe_allow_html=True)




 st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #FF69B4; font-family: 'Courier New', Courier, monospace; font-size: 60px; text-shadow: 0 0 10px #FF69B4, 0 0 20px #FF69B4;">
            Fantasy World
        </h1>
        <h3 style="color: #00CED1; font-family: 'Courier New', Courier, monospace; font-size: 25px; text-shadow: 0 0 5px #00CED1;">
            Search, Watch, and Feel the Magic of Entertainment ✨
        </h3>
    </div>
""", unsafe_allow_html=True)
 

# st.title("🎵 Music Selection App")
 option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'],key='home')
 if option=='Home':
  st.header("Music for You",divider='rainbow')
  left, middle, right = st.columns(3, vertical_alignment='center')
  # 1st song
  # english music
  s1=df.sample(n=1)
  song=s1["song_name"].iloc[0]
  poster=s1['poster'].iloc[0]
  left.image(poster,width=150)
  with left:
   st.write(song)
# 2nd song
  s2=df.sample(n=1)
  song1=s2["song_name"].iloc[0]  
  poster1=s2['poster'].iloc[0]
  middle.image(poster1,width=150)
  with middle:
   st.write(song1)
  # 3rd song
  s3=df.sample(n=1)
  song2=s3["song_name"].iloc[0]
  poster2=s3['poster'].iloc[0]
  right.image(poster2,width=150)
  with right:
    st.write(song2)
  left, middle, right = st.columns(3, vertical_alignment='center')

#  movies
  df2=pd.read_csv("movieorig.csv",encoding='ISO-8859-1')
  st.header("Movies For You",divider='green')
  left, middle, right = st.columns(3, vertical_alignment='center')
  # 1st movie
  m1=df2.sample(n=1)
  mo=m1["Title"].iloc[0]
  mposter=m1['poster_path'].iloc[0]
  left.image(mposter,width=150)
  with left:
    st.write(mo)
# 2nd song
  m2=df2.sample(n=1)
  mmo=m2["Title"].iloc[0]
  mmposter=m2['poster_path'].iloc[0]
  middle.image(mmposter,width=150)
  with middle:
    st.write(mmo)
    # 3rd song
  m3=df2.sample(n=1)
  mmmo2=m3["Title"].iloc[0]
  mmmposter2=m3['poster_path'].iloc[0]
  right.image(mmmposter2,width=150)
  with right:
    st.write(mmmo2)
# # kdrama
#  df3=pd.read_csv("kdrama1.csv",encoding='ISO-8859-1')
  st.header("K-Drama for You",divider='blue')
  left, middle, right = st.columns(3, vertical_alignment='center')
  
# 1st movie
  k1=dfk.sample(n=1)
  kd=k1["Name"].iloc[0]
  kposter=k1['Poster Path'].iloc[0]
  left.image(kposter,width=150)
  with left:
    st.write(kd)
# 2nd song
  k2=dfk.sample(n=1)
  kk=k2["Name"].iloc[0]
  kkposter=k2['Poster Path'].iloc[0]
  middle.image(kkposter,width=150)
  with middle:
    st.write(kk)
  # 3rd song
  k3=dfk.sample(n=1)
  kk3=k3["Name"].iloc[0]
  kkposter2=k3['Poster Path'].iloc[0]
  right.image(kkposter2,width=150)
  with right:
    st.write(kk3)
  if 'page' not in st.session_state:
        st.session_state.page = "Home"

 elif option == 'Music':
          st.session_state.page = "Music"
          if st.session_state.page == "Music":
            music.show()
 elif option == 'Movies':
          st.session_state.page = "Movies"
          if st.session_state.page=='Movies':
              movie.show()
 elif option == 'K-Drama':
          st.session_state.page = "kdrama"
          if st.session_state.page=='kdrama':
              kdrama.show()
 else:
          st.write("")
          




    

    