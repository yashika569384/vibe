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
import everyonecos
import everten
import teen
import mature

# home
# st.set_page_config(page_title='Gaming')


df3=pd.read_csv('gamesff.csv',encoding='ISO-8859-1')
def show():
 st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #FF69B4; font-family: 'Courier New', Courier, monospace; font-size: 60px; text-shadow: 0 0 10px #FF69B4, 0 0 20px #FF69B4;">
            Gamify
        </h1>
        <h3 style="color: #00CED1; font-family: 'Courier New', Courier, monospace; font-size: 25px; text-shadow: 0 0 5px #00CED1;">
            Where every game is an epic journey. ✨
        </h3>
    </div>
""", unsafe_allow_html=True)
 st.title(":red[Games]")
 sidebar=st.sidebar.selectbox(label="Select options",options=['Home','Game'])

 if sidebar=='Home':
 

  left, middle, right = st.columns(3, vertical_alignment='center')
  g1=df3.sample(n=1)
  game=g1["Name"].iloc[0]
  poster=g1['Poster'].iloc[0]
  left.image(poster,width=150)
  with left:
   st.write(game)
# 2nd song
  g2=df3.sample(n=1)
  game1=g2["Name"].iloc[0]  
  poster1=g2['Poster'].iloc[0]
  middle.image(poster1,width=150)
  with middle:
   st.write(game1)
  # 3rd song
  g3=df3.sample(n=1)
  game2=g3["Name"].iloc[0]
  poster2=g3['Poster'].iloc[0]
  right.image(poster2,width=150)
  with right:
    st.write(game2)
  left, middle, right = st.columns(3, vertical_alignment='center')
  g4=df3.sample(n=1)
  game3=g4["Name"].iloc[0]
  poster3=g4['Poster'].iloc[0]
  left.image(poster3,width=150)
  with left:
    st.write(game3)
# 2nd song
  g5=df3.sample(n=1)
  game4=g5["Name"].iloc[0]   
  poster4=g5['Poster'].iloc[0]
  middle.image(poster4,width=150)
  with middle:
    st.write(game4)
    # 3rd song
  g6=df3.sample(n=1)
  game5=g6["Name"].iloc[0]
  poster5=g6['Poster'].iloc[0]
  right.image(poster5,width=150)
  with right:
    st.write(game5)
  left, middle, right = st.columns(3, vertical_alignment='center')
  g7=df3.sample(n=1)
  game6=g7["Name"].iloc[0]
  poster6=g7['Poster'].iloc[0]
  left.image(poster6,width=150)
  with left:
    st.write(game6)
# 2nd song
  g8=df3.sample(n=1)
  game7=g8["Name"].iloc[0]  
  poster7=g8['Poster'].iloc[0]
  middle.image(poster7,width=150)
  with middle:
    st.write(game7)
  # 3rd song
  g9=df3.sample(n=1)
  game8=g9["Name"].iloc[0]
  poster8=g9['Poster'].iloc[0]
  right.image(poster8,width=150)
  with right:
    st.write(game8)
 if sidebar=='Game':
  search_query = st.text_input(label="Search for a game")
  if search_query:
   if len(search_query) >= 3:
    fil_df=df3[df3.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
    if not fil_df.empty:
     st.subheader("Search Results:")
     if len(fil_df)==1:
      ga=fil_df['Name'].iloc[0]
      img=fil_df['Poster'].iloc[0]     
      st.image(img,width=200)
     
      st.write(ga)
        # st.write('Platform:',p)

      pl=fil_df['Platform'].iloc[0]
      st.write('Platform:',pl)
     else:
       lef,mid=st.columns(2)
       img1=fil_df['Poster'].iloc[0]
       img2=fil_df['Poster'].iloc[1]
       pl1=fil_df['Platform'].iloc[0]
       pl2=fil_df['Platform'].iloc[1]   
      
      
       ga1=fil_df['Name'].iloc[0]
       ga2=fil_df['Name'].iloc[1]
       lef.image(img1,width=200)
       with lef:
        st.write(ga1)
        st.write('Platform:',pl1)
      #  if st.button("▶ Play",key="re_lef"):
      #   talk_l(s1)
      #   play_songs(s1)
      #   play(s1)
      
       mid.image(img2,width=200)
       with mid:
        st.write(ga2)
        st.write('Platform:',pl2)
      #  if st.button("▶ Play",key="re_mid"):
      #   talk_m(s2)
      #   play_songs(s2)
      #   play(s2)
  else:
   print("")


  rating=st.selectbox("Select Rating:",['Everyone','Above 10 years','Teens','Mature'])

  if rating=="Everyone":
   everyonecos.show()
  elif rating=="Above 10 years":
   everten.show()
  elif rating=="Teens":
   teen.show()
  elif rating=="Mature":
   mature.show()