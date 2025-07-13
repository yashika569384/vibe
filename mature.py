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
dfm=pd.read_csv('mature.csv',encoding='ISO-8859-1')
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
  if 'songs_mselected' not in st.session_state:
    st.session_state.songs_mselected = random.sample(dfm.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_mleft = st.session_state.songs_mselected[0]
    st.session_state.current_song_mmiddle = st.session_state.songs_mselected[1]
    st.session_state.current_song_mright = st.session_state.songs_mselected[2]
    st.session_state.current_song_mle = st.session_state.songs_mselected[3]
    st.session_state.current_song_mmi = st.session_state.songs_mselected[4]
    st.session_state.current_song_mri = st.session_state.songs_mselected[5]
    st.session_state.current_song_mlee = st.session_state.songs_mselected[6]
    st.session_state.current_song_mmii = st.session_state.songs_mselected[7]
    st.session_state.current_song_mrii = st.session_state.songs_mselected[8]
    
    left, middle, right = st.columns(3)
    songm1 = st.session_state.current_song_mleft
    songm2=st.session_state.current_song_mmiddle
    songm3=st.session_state.current_song_mright
    songm4= st.session_state.current_song_mle 
    songm5= st.session_state.current_song_mmi
    songm6= st.session_state.current_song_mri
    songm7=st.session_state.current_song_mlee
    songm8=st.session_state.current_song_mmii
    songm9=st.session_state.current_song_mrii

    s_lm=songm1['Name']
    s_mm=songm2['Name']
    s_rm=songm3['Name']
    s_lem=songm4['Name']
    s_mim=songm5['Name']
    s_rim=songm6['Name']
    s_leem=songm7['Name']
    s_miim=songm8['Name']
    s_riim=songm9['Name']

  dfm['combined_features']=dfm['Genre']+dfm['Rating']
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  c=cv.fit_transform(dfm['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
      idx=dfm[dfm['Name']==song_name].index[0]
      distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda vector:vector[1])
# 
      s=[dfm.iloc[i[0]] for i in distance[1:7]]
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
  songm1 = st.session_state.current_song_mleft
  songm2=st.session_state.current_song_mmiddle
  songm3=st.session_state.current_song_mright
  songm4= st.session_state.current_song_mle 
  songm5= st.session_state.current_song_mmi
  songm6= st.session_state.current_song_mri
  songm7=st.session_state.current_song_mlee
  songm8=st.session_state.current_song_mmii
  songm9=st.session_state.current_song_mrii
  s_lm=songm1['Name']
  s_mm=songm2['Name']
  s_rm=songm3['Name']
  s_lem=songm4['Name']
  s_mim=songm5['Name']
  s_rim=songm6['Name']
  s_leem=songm7['Name']
  s_miim=songm8['Name']
  s_riim=songm9['Name']
  left, middle, right = st.columns(3)              
  left.image(songm1['Poster'], width=150)
  with left:
     st.write(s_lm)
     if st.button("Recommendations:",key='rec_lefte'):
      recommand(s_lm)
  middle.image(songm2['Poster'], width=150)
  with middle:
     st.write(s_mm)
     if st.button("Recommendations:",key='rec_middlee'):
      recommand(s_mm)
  right.image(songm3['Poster'], width=150)
  with right:
    st.write(s_rm)
    if st.button("Recommendations", key="play_erighte"):
  # v=s_l
     recommand(s_rm)
  le, mi, ri = st.columns(3)
  with le:
   song4= st.session_state.current_song_mle
   st.image(songm4['Poster'], width=150)
   st.write(songm4['Name'])
   if st.button("Recommendations:", key="play_elee"):
      recommand(s_lem)
  with mi:
    song5 = st.session_state.current_song_mmi
    st.image(songm5['Poster'], width=150)
    st.write(songm5['Name'])
    if st.button("Recommendations", key="play_emie"):
      recommand(s_mim)
  with ri:
    song6 = st.session_state.current_song_mri
    st.image(songm6['Poster'], width=150)
    st.write(songm6['Name'])
    if st.button("Recommendations", key="play_erie"):
      recommand(s_rim)
  lee, mii, rii = st.columns(3)
  with lee:
    songm7= st.session_state.current_song_mlee
    st.image(songm7['Poster'], width=150)
    st.write(songm7['Name'])
    if st.button("REcommendations", key="play_eleee"):
      recommand(s_leem)
  with mii:
    song8 = st.session_state.current_song_mmii
    st.image(song8['Poster'], width=150)
    st.write(song8['Name'])
    if st.button("Recommendations", key="play_emiie"):
      recommand(s_miim)
  with rii:
    song9 = st.session_state.current_song_mrii
    st.image(song9['Poster'], width=150)
    st.write(song9['Name'])
    if st.button("Recommendations", key="play_eriie"):
      recommand(s_riim)
# Right Column - "Now Playing
# show()