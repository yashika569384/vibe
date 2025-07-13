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
dft=pd.read_csv('teens.csv',encoding='ISO-8859-1')
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
  if 'songs_tselected' not in st.session_state:
    st.session_state.songs_tselected = random.sample(dft.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_tleft = st.session_state.songs_tselected[0]
    st.session_state.current_song_tmiddle = st.session_state.songs_tselected[1]
    st.session_state.current_song_tright = st.session_state.songs_tselected[2]
    st.session_state.current_song_tle = st.session_state.songs_tselected[3]
    st.session_state.current_song_tmi = st.session_state.songs_tselected[4]
    st.session_state.current_song_tri = st.session_state.songs_tselected[5]
    st.session_state.current_song_tlee = st.session_state.songs_tselected[6]
    st.session_state.current_song_tmii = st.session_state.songs_tselected[7]
    st.session_state.current_song_trii = st.session_state.songs_tselected[8]
    
    left, middle, right = st.columns(3)
    songt1 = st.session_state.current_song_tleft
    songt2=st.session_state.current_song_tmiddle
    songt3=st.session_state.current_song_tright
    songt4= st.session_state.current_song_tle 
    songt5= st.session_state.current_song_tmi
    songt6= st.session_state.current_song_tri
    songt7=st.session_state.current_song_tlee
    songt8=st.session_state.current_song_tmii
    songt9=st.session_state.current_song_trii

    s_lt=songt1['Name']
    s_mt=songt2['Name']
    s_rt=songt3['Name']
    s_let=songt4['Name']
    s_mit=songt5['Name']
    s_rit=songt6['Name']
    s_leet=songt7['Name']
    s_miit=songt8['Name']
    s_riit=songt9['Name']

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
  songt1 = st.session_state.current_song_tleft
  songt2=st.session_state.current_song_tmiddle
  songt3=st.session_state.current_song_tright
  songt4= st.session_state.current_song_tle 
  songt5= st.session_state.current_song_tmi
  songt6= st.session_state.current_song_tri
  songt7=st.session_state.current_song_tlee
  songt8=st.session_state.current_song_tmii
  songt9=st.session_state.current_song_trii
  s_lt=songt1['Name']
  s_mt=songt2['Name']
  s_rt=songt3['Name']
  s_let=songt4['Name']
  s_mit=songt5['Name']
  s_rit=songt6['Name']
  s_leet=songt7['Name']
  s_miit=songt8['Name']
  s_riit=songt9['Name']
  left, middle, right = st.columns(3)              
  left.image(songt1['Poster'], width=150)
  with left:
     st.write(s_lt)
     if st.button("Recommendations:",key='rec_left'):
      recommand(s_lt)
  middle.image(songt2['Poster'], width=150)
  with middle:
     st.write(s_mt)
     if st.button("Recommendations:",key='rec_middle'):
      recommand(s_mt)
  right.image(songt3['Poster'], width=150)
  with right:
    st.write(s_rt)
    if st.button("Recommendations", key="play_eright"):
  # v=s_l
     recommand(s_rt)
  le, mi, ri = st.columns(3)
  with le:
   songt4= st.session_state.current_song_tle
   st.image(songt4['Poster'], width=150)
   st.write(songt4['Name'])
   if st.button("Recommendations:", key="play_ele"):
      recommand(s_let)
  with mi:
    songt5 = st.session_state.current_song_tmi
    st.image(songt5['Poster'], width=150)
    st.write(songt5['Name'])
    if st.button("Recommendations", key="play_emi"):
      recommand(s_mit)
  with ri:
    songt6 = st.session_state.current_song_tri
    st.image(songt6['Poster'], width=150)
    st.write(songt6['Name'])
    if st.button("Recommendations", key="play_eri"):
      recommand(s_rit)
  lee, mii, rii = st.columns(3)
  with lee:
    songt7= st.session_state.current_song_tlee
    st.image(songt7['Poster'], width=150)
    st.write(songt7['Name'])
    if st.button("REcommendations", key="play_elee"):
      recommand(s_leet)
  with mii:
    songt8 = st.session_state.current_song_tmii
    st.image(songt8['Poster'], width=150)
    st.write(songt8['Name'])
    if st.button("Recommendations", key="play_emii"):
      recommand(s_miit)
  with rii:
    songt9 = st.session_state.current_song_trii
    st.image(songt9['Poster'], width=150)
    st.write(songt9['Name'])
    if st.button("Recommendations", key="play_erii"):
      recommand(s_riit)
# Right Column - "Now Playing
# show()