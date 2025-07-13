import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import streamlit as st
import urllib
import pandas as pd
dft=pd.read_csv('Everyone10+.csv',encoding='ISO-8859-1')
def show():
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
          padding: 20px 35px;
          font-size: 100px;
          width: 200px ;
          height: 50px ;
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
#  search_query = st.text_input("Search for a song")
#  if search_query:
#      if len(search_query) >= 3:
#       fil_df=dft[dft.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
#       if not fil_df.empty:
#        st.subheader("Search Results:")
#        if len(fil_df)==1:
#          img=fil_df['Poster'].iloc[0]
#          st.image(img,width=200)
#          s=fil_df['Name'].iloc[0]
#        else:
#         lef, mid = st.columns(2)
#         img1=fil_df['Poster'].iloc[0]
#         img2=fil_df['Poster'].iloc[1]
#         s1=fil_df['Name'].iloc[0]
#         s2=fil_df['Name'].iloc[1]
  import random
  if 'songs_etselected' not in st.session_state:
    st.session_state.songs_etselected = random.sample(dft.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_etleft = st.session_state.songs_etselected[0]
    st.session_state.current_song_etmiddle = st.session_state.songs_etselected[1]
    st.session_state.current_song_etright = st.session_state.songs_etselected[2]
    st.session_state.current_song_etle = st.session_state.songs_etselected[3]
    st.session_state.current_song_etmi = st.session_state.songs_etselected[4]
    st.session_state.current_song_etri = st.session_state.songs_etselected[5]
    st.session_state.current_song_etlee = st.session_state.songs_etselected[6]
    st.session_state.current_song_etmii = st.session_state.songs_etselected[7]
    st.session_state.current_song_etrii = st.session_state.songs_etselected[8]
    
    left, middle, right = st.columns(3)
    songet1 = st.session_state.current_song_etleft
    songet2=st.session_state.current_song_etmiddle
    songet3=st.session_state.current_song_etright
    songet4= st.session_state.current_song_etle 
    songet5= st.session_state.current_song_etmi
    songet6= st.session_state.current_song_etri
    songet7=st.session_state.current_song_etlee
    songet8=st.session_state.current_song_etmii
    songet9=st.session_state.current_song_etrii

    s_let=songet1['Name']
    s_met=songet2['Name']
    s_ret=songet3['Name']
    s_leet=songet4['Name']
    s_miet=songet5['Name']
    s_riet=songet6['Name']
    s_leeet=songet7['Name']
    s_miiet=songet8['Name']
    s_riiet=songet9['Name']

  dft['combined_features']=dft['Genre']+dft['Rating']
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  c=cv.fit_transform(dft['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
      idx=dft[dft['Name']==song_name].index[0]
      distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda vector:vector[1])
# 
      s=[dft.iloc[i[0]] for i in distance[1:7]]
#  random.shuffle(s1)
  
      rec = random.sample(s, min(len(s), 7))
      for song in rec: 
#  st.write(s1)
       songs = song['Name']
       poster_url = song['Poster']    # ✅ Access poster directly
       st.image(poster_url, width=150)
       st.write(songs)
  import urllib
  import requests
  songet1 = st.session_state.current_song_etleft
  songet2=st.session_state.current_song_etmiddle
  songet3=st.session_state.current_song_etright
  songet4= st.session_state.current_song_etle 
  songet5= st.session_state.current_song_etmi
  songet6= st.session_state.current_song_etri
  songet7=st.session_state.current_song_etlee
  songet8=st.session_state.current_song_etmii
  songet9=st.session_state.current_song_etrii
  s_let=songet1['Name']
  s_met=songet2['Name']
  s_ret=songet3['Name']
  s_leet=songet4['Name']
  s_miet=songet5['Name']
  s_riet=songet6['Name']
  s_leeet=songet7['Name']
  s_miiet=songet8['Name']
  s_riiet=songet9['Name']
  left, middle, right = st.columns(3)              
  left.image(songet1['Poster'], width=150)
  with left:
     st.write(s_let)
     if st.button("Recommendations:",key='etleftg'):
      recommand(s_let)
  middle.image(songet2['Poster'], width=150)
  with middle:
     st.write(s_met)
     if st.button("Recommendations:",key='etmiddleg'):
      recommand(s_met)
  right.image(songet3['Poster'], width=150)
  with right:
     st.write(s_ret)
     if st.button("Recommendations:",key='etrightg'):
      recommand(s_ret)
  le, mi, ri = st.columns(3)
  with le:
   songet4= st.session_state.current_song_etle
   st.image(songet4['Poster'], width=150)
   st.write(songet4['Name'])
   if st.button("Recommendations:", key="etleg"):
      recommand(s_leet)
  with mi:
    songet5 = st.session_state.current_song_etmi
    st.image(songet5['Poster'], width=150)
    st.write(songet5['Name'])
    if st.button("Recommendations", key="etmig"):
      recommand(s_miet)
  with ri:
    songet6 = st.session_state.current_song_etri
    st.image(songet6['Poster'], width=150)
    st.write(songet6['Name'])
    if st.button("Recommendations", key="etrig"):
      recommand(s_riet)
  lee, mii, rii = st.columns(3)
  with lee:
    songet7= st.session_state.current_song_etlee
    st.image(songet7['Poster'], width=150)
    st.write(songet7['Name'])
    if st.button("Recommendations", key="etleeg"):
      recommand(s_leeet)
  with rii:
    songet8= st.session_state.current_song_etrii
    st.image(songet8['Poster'], width=150)
    st.write(songet8['Name'])
    if st.button("Recommendations", key="etriig"):
      recommand(s_miiet)
  with mii:
    songet9= st.session_state.current_song_etmii
    st.image(songet9['Poster'], width=150)
    st.write(songet9['Name'])
    if st.button("Recommendations", key="etmiig"):
      recommand(s_riiet)
# show()