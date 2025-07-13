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
dfe=pd.read_csv('everyone.csv',encoding='ISO-8859-1')

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
        padding: 25px 35px;
        font-size: 100px;
        width: 230px;
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
  if 'songs_eselected' not in st.session_state:
    st.session_state.songs_eselected = random.sample(dfe.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_eleft = st.session_state.songs_eselected[0]
    st.session_state.current_song_emiddle = st.session_state.songs_eselected[1]
    st.session_state.current_song_eright = st.session_state.songs_eselected[2]
    st.session_state.current_song_ele = st.session_state.songs_eselected[3]
    st.session_state.current_song_emi = st.session_state.songs_eselected[4]
    st.session_state.current_song_eri = st.session_state.songs_eselected[5]
    st.session_state.current_song_elee = st.session_state.songs_eselected[6]
    st.session_state.current_song_emii = st.session_state.songs_eselected[7]
    st.session_state.current_song_erii = st.session_state.songs_eselected[8]
    
    left, middle, right = st.columns(3)
    songe1 = st.session_state.current_song_eleft
    songe2=st.session_state.current_song_emiddle
    songe3=st.session_state.current_song_eright
    songe4= st.session_state.current_song_ele 
    songe5= st.session_state.current_song_emi
    songe6= st.session_state.current_song_eri
    songe7=st.session_state.current_song_elee
    songe8=st.session_state.current_song_emii
    songe9=st.session_state.current_song_erii

    s_le=songe1['Name']
    s_me=songe2['Name']
    s_re=songe3['Name']
    s_lee=songe4['Name']
    s_mie=songe5['Name']
    s_rie=songe6['Name']
    s_leee=songe7['Name']
    s_miie=songe8['Name']
    s_riie=songe9['Name']

  dfe['combined_features']=dfe['Genre']+dfe['Rating']
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  c=cv.fit_transform(dfe['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
      idx=dfe[dfe['Name']==song_name].index[0]
      distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda vector:vector[1])
# 
      s=[dfe.iloc[i[0]] for i in distance[1:7]]
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
  songe1=st.session_state.current_song_eleft
  songe2=st.session_state.current_song_emiddle
  songe3=st.session_state.current_song_eright
  songe4= st.session_state.current_song_ele 
  songe5= st.session_state.current_song_emi
  songe6= st.session_state.current_song_eri
  songe7=st.session_state.current_song_elee
  songe8=st.session_state.current_song_emii
  songe9=st.session_state.current_song_erii
  s_le=songe1['Name']
  s_me=songe2['Name']
  s_re=songe3['Name']
  s_lee=songe4['Name']
  s_mie=songe5['Name']
  s_rie=songe6['Name']
  s_leee=songe7['Name']
  s_miie=songe8['Name']
  s_riie=songe9['Name']
  left, middle, right = st.columns(3)              
  left.image(songe1['Poster'], width=150)
  with left:
     st.write(s_le)
     if st.button("Recommendations:",key='rec_lefte'):
      recommand(s_le)
  middle.image(songe2['Poster'], width=150)
  with middle:
     st.write(s_me)
     if st.button("Recommendations:",key='rec_middlee'):
      recommand(s_me)
  right.image(songe3['Poster'], width=150)
  with right:
    st.write(s_re)
    if st.button("Recommendations:", key="play_erighte"):
      recommand(s_re)
  le, mi, ri = st.columns(3)
  with le:
   songe4= st.session_state.current_song_ele
   st.image(songe4['Poster'], width=150)
   st.write(songe4['Name'])
   if st.button("Recommendation", key="play_ele"):
      
      recommand(s_lee)
  with mi:
    songe5 = st.session_state.current_song_emi
    st.image(songe5['Poster'], width=150)
    st.write(songe5['Name'])
    if st.button("Recommend", key="play_emie"):
      
      recommand(s_mie)
  with ri:
    songe6 = st.session_state.current_song_eri
    st.image(songe6['Poster'], width=150)
    st.write(songe6['Name'])
    if st.button("Recommendation:", key="play_erie"):
  
      recommand(s_rie)
  lee, mii, rii = st.columns(3)
  with lee:
    songe7= st.session_state.current_song_elee
    st.image(songe7['Poster'], width=150)
    st.write(songe7['Name'])
    if st.button("Recommendation:", key="play_eleee"):
      
      recommand(s_leee)
# Middle Column - Fixed Song 2
  with mii:
    songe8 = st.session_state.current_song_emii
    st.image(songe8['Poster'], width=150)
    st.write(songe8['Name'])
    if st.button("Recomendation:", key="play_emiie"):
      
      recommand(s_miie)

# Right Column - "Now Playing" Section
  with rii:
    songe9 = st.session_state.current_song_erii
    st.image(songe9['Poster'], width=150)
    st.write(songe9['Name'])
    if st.button("Recommendation:", key="play_eriie"):
      
      recommand(s_riie)   
# show()  