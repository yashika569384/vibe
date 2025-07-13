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
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
df1=pd.read_csv('englishmusic.csv',encoding='ISO-8859-1')
df2=pd.read_csv('hindimusic.csv',encoding='ISO-8859-1')
df3=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')

def show():
  st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/free-vector/gradient-style-network-connection-background_23-2148879891.jpg?semt=ais_hybrid&w=740');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True
)
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
  search_query = st.text_input("Search for a song")
  if search_query:
     if len(search_query) >= 3:
      fil_df=df[df.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
      if not fil_df.empty:
       st.subheader("Search Results:")
       if len(fil_df)==1:
        img=fil_df['poster'].iloc[0]
        st.image(img,width=200)
        s=fil_df['song_name'].iloc[0]
        st.write(s)
        import urllib
        import requests
        def talk_l(s):
         engine = pyttsx3.init()
         engine.say(s)
         engine.runAndWait()
        def play_songs(s):
             if (s):
              st.write(f"Playing the song: {s}")
              
              query = urllib.parse.quote(s + " official audio")
              url=f"https://www.youtube.com/results?search_query={s}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
              # else:


              #    return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
             else:
                st.write("Please provide a song name.")
                talk_l("Please provide a song name.")
        #  play_songs(s_l)
        def play(s):
              url = play_songs(s)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
      
        if st.button("▶ Play"):
         talk_l(s)
         play_songs(s)
         play(s)
         st.write(s)
    #  st.write(s1)
       else: 
          lef, mid = st.columns(2)
          img1=fil_df['poster'].iloc[0]
          img2=fil_df['poster'].iloc[1]
          
          
          s1=fil_df['song_name'].iloc[0]
          s2=fil_df['song_name'].iloc[1]
          
       def talk_l(s1):
         engine = pyttsx3.init()
         engine.say(s1)
         engine.runAndWait()
       def play_songs(s1):
             if (s1):
              st.write(f"Playing the song: {s1}")
              
              query = urllib.parse.quote(s1 + " official audio")
              url=f"https://www.youtube.com/results?search_query={s1}"
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
              # else:
              #    return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
             else:
                st.write("Please provide a song name.")
                talk_l("Please provide a song name.")
       def play(s1):
              url = play_songs(s1)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
       def talk_m(s2):
         engine = pyttsx3.init()
         engine.say(s2)
         engine.runAndWait()
         def play_songs(s2):
             if (s2):
              st.write(f"Playing the song: {s2}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s2 + " official audio")
              url=f"https://www.youtube.com/results?search_query={s2}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a song name.")
                talk_m("Please provide a song name.")
        #  play_songs(s_l)
             def play(s2):
              url = play_songs(s2)
              if url:
                st.markdown(
                   f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
             play(s2)
       lef.image(img1,width=200)
       with lef:
         st.write(s1)
         if st.button("▶ Play",key="re_lefh"):
          talk_l(s1)
          play_songs(s1)
          play(s1)
      
      #  mid.image(img2,width=200)
      # Defensive check before displaying the image
      if img2 is not None:
       try:
        mid.image(img2, width=200)
       except Exception as e:
        st.warning(f"Couldn't load image for middle column: {e}")
      else:
       st.warning("No image available for the middle column.")

       with mid:
         st.write(s2)
         if st.button("▶ Play",key="re_midh"):
          try:
            talk_m(s2)
            play_songs(s2)
            play(s2)
          except IndexError:
            st.error("Could not play the content for the left column. Data might be missing.")
          except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
         else:
          st.write("Song does not exist")
  else:
      st.write("")
  dme=df2[df2['language']=='Hindi']
  import random
  dme=df2[df2['language']=='Hindi']
  if 'songs_hselected' not in st.session_state:
    st.session_state.songs_hselected = random.sample(dme.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_lefth = st.session_state.songs_hselected[0]
    st.session_state.current_song_middleh = st.session_state.songs_hselected[1]
    st.session_state.current_song_righth = st.session_state.songs_hselected[2]
    st.session_state.current_song_leh = st.session_state.songs_hselected[3]
    st.session_state.current_song_mih = st.session_state.songs_hselected[4]
    st.session_state.current_song_rih = st.session_state.songs_hselected[5]
    st.session_state.current_song_leeh = st.session_state.songs_hselected[6]
    st.session_state.current_song_miih = st.session_state.songs_hselected[7]
    st.session_state.current_song_riih = st.session_state.songs_hselected[8]
# Layout columns
    left, middle, right = st.columns(3)
    songh1 = st.session_state.current_song_lefth
    songh2=st.session_state.current_song_middleh
    songh3=st.session_state.current_song_righth
    songh4= st.session_state.current_song_leh 
    songh5= st.session_state.current_song_mih
    songh6= st.session_state.current_song_rih
    songh7=st.session_state.current_song_leeh
    songh8=st.session_state.current_song_miih
    songh9=st.session_state.current_song_riih

    s_lh=songh1['song_name']
    s_mh=songh2['song_name']
    s_rh=songh3['song_name']
    s_leh=songh4['song_name']
    s_mih=songh5['song_name']
    s_rih=songh6['song_name']
    s_leeh=songh7['song_name']
    s_miih=songh8['song_name']
    s_riih=songh9['song_name']

  def talk_r(s_rh):
         engine = pyttsx3.init()
         engine.say(s_rh)
         engine.runAndWait()
         def play_songs(s_rh):
             if (s_rh):
              st.write(f"Playing the song: {s_rh}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_rh + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_rh}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
              else:
               return None
              
             else:
                st.write("Please provide a song name.")
                talk_r("Please provide a song name.")
        #  play_songs(s_l)
         def play(s_rh):
              url = play_songs(s_rh)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_rh)



  
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  df2['combined_features']=df2['Genre']+df2['language']
  c=cv.fit_transform(df2['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
# similarity
  ds2  = df2.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
  import random
# l, m, r = st.columns(3) 
  def recommand(song_name):
    index=df2[df2['song_name']==song_name].index[0]
    distance1 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    s=[df2.iloc[i[0]] for i in distance1[1:7]]  
    rec = random.sample(s, min(len(s), 7))
    for song in rec: 
     songs = song['song_name']
     poster_url = song['poster']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
  import urllib
  import requests
  def talk_l(s_lh):
        engine = pyttsx3.init()
        engine.say(s_lh)
        engine.runAndWait()
        def play_songs(s_lh):
            if (s_lh):
             st.write(f"Playing the song: {s_lh}")
            query = urllib.parse.quote(s_lh + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lh}"
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
        def play(s_lh):
            url = play_songs(s_lh)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lh)

  def talk_m(s_mh):
        engine = pyttsx3.init()
        engine.say(s_mh)
        engine.runAndWait()
        def play_songs(s_mh):
            if (s_mh):
              st.write(f"Playing the song: {s_mh}")
            query = urllib.parse.quote(s_mh + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mh}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            
            else:
              st.write("Please provide a song name.")
              talk_m("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_mh):
            url = play_songs(s_mh)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mh)
  if 'songs_hselected' not in st.session_state:
    st.session_state.current_song_lefth = st.session_state.songs_hselected[0]
    st.session_state.current_song_middleh = st.session_state.songs_hselected[1]
    st.session_state.current_song_righth = st.session_state.songs_hselected[2]
    st.session_state.current_song_leh = st.session_state.songs_hselected[3]
    st.session_state.current_song_mih = st.session_state.songs_hselected[4]
    st.session_state.current_song_rih = st.session_state.songs_hselected[5]
    st.session_state.current_song_leeh = st.session_state.songs_hselected[6]
    st.session_state.current_song_miih = st.session_state.songs_hselected[7]
    st.session_state.current_song_riih = st.session_state.songs_hselected[8]

  songh1 = st.session_state.current_song_lefth
  songh2=st.session_state.current_song_middleh
  songh3=st.session_state.current_song_righth
  songh4= st.session_state.current_song_leh 
  songh5= st.session_state.current_song_mih
  songh6= st.session_state.current_song_rih
  songh7=st.session_state.current_song_leeh
  songh8=st.session_state.current_song_miih
  songh9=st.session_state.current_song_riih
  s_lh=songh1['song_name']
  s_mh=songh2['song_name']
  s_rh=songh3['song_name']
  s_leh=songh4['song_name']
  s_mih=songh5['song_name']
  s_rih=songh6['song_name']
  s_leeh=songh7['song_name']
  s_miih=songh8['song_name']
  s_riih=songh9['song_name']
  left, middle, right = st.columns(3)              
  left.image(songh1['poster'], width=150)
  with left:
    st.write(s_lh)
    if st.button("▶ Play", key="play_elefth"):
      talk_l(s_lh)
      st.subheader("Made For You:")
      recommand(s_lh)   
    
  middle.image(songh2['poster'], width=150)
  with middle:
    st.write(s_mh)
    if st.button("▶ Play", key="play_emiddleh"):
      talk_m(s_mh)     
      recommand(s_mh)
  right.image(songh3['poster'], width=150)
  with right:
    st.write(s_rh)
    if st.button("▶ Play", key="play_erighth"):
     talk_r(s_rh)
     recommand(s_rh)
  import requests
  def talk_le(s_leh):
        engine = pyttsx3.init()
        engine.say(s_leh)
        engine.runAndWait()
        def play_songs(s_leh):
            if (s_leh):
             st.write(f"Playing the song: {s_leh}")
            query = urllib.parse.quote(s_leh + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_leh}"
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              st.write("Please provide a song name.")
              talk_le("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_leh):
            url = play_songs(s_leh)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_leh)


  def talk_mi(s_mih):
        engine = pyttsx3.init()
        engine.say(s_mih)
        engine.runAndWait()
        def play_songs(s_mih):
            if (s_mih):
             st.write(f"Playing the song: {s_mih}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mih + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mih}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_mi("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_mih):
            url = play_songs(s_mih)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mih)
  import urllib
  def talk_ri(s_rih):
        engine = pyttsx3.init()
        engine.say(s_rih)
        engine.runAndWait()
        def play_songs(s_rih):
            if (s_rih):
             st.write(f"Playing the song: {s_rih}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rih + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_rih}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_r("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_rih):
            url = play_songs(s_rih)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rih)

# Left Column - Fixed Song. 2nd column
  le, mi, ri = st.columns(3)
  with le:
   songh4= st.session_state.current_song_leh
   st.image(songh4['poster'], width=150)
   st.write(songh4['song_name'])
   if st.button("▶ Play", key="play_eleh"):
      talk_le(s_leh)
      recommand(s_leh)
  
# Middle Column - Fixed Song 2
  with mi:
    songh5 = st.session_state.current_song_mih
    st.image(songh5['poster'], width=150)
    st.write(songh5['song_name'])
    if st.button("▶ Play", key="play_emih"):
      talk_mi(s_mih)
      recommand(s_mih)
      

# Right Column - "Now Playing" Section
  with ri:
    songh6 = st.session_state.current_song_rih
    st.image(songh6['poster'], width=150)
    st.write(songh6['song_name'])
    if st.button("▶ Play", key="play_eri"):
      talk_ri(s_rih)
      recommand(s_rih)
      
      # 3rd row
  lee, mii, rii = st.columns(3)
  def talk_lee(s_leeh):
        engine = pyttsx3.init()
        engine.say(s_leeh)
        engine.runAndWait()
        def play_songs(s_leeh):
            if (s_leeh):
             st.write(f"Playing the song: {s_leeh}")
            query = urllib.parse.quote(s_leeh + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_leeh}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_lee("Please provide a song name.")
      #  play_songs_l)
        def play(s_leeh):
            url = play_songs(s_leeh)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_leeh)
  def talk_mii(s_miih):
        engine = pyttsx3.init()
        engine.say(s_miih)
        engine.runAndWait()
        def play_songs(s_miih):
            if (s_miih):
             st.write(f"Playing the song: {s_miih}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miih + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_miih}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_mii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_miih):
            url = play_songs(s_miih)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_miih)
  def talk_rii(s_riih):
        engine = pyttsx3.init()
        engine.say(s_riih)
        engine.runAndWait()
        def play_songs(s_riih):
            if (s_riih):
             st.write(f"Playing the song: {s_riih}")
            
            
            query = urllib.parse.quote(s_riih + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_riih}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_rii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_riih):
            url = play_songs(s_riih)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_riih)
# Left Column - Fixed Song 1
  with lee:
    songh7= st.session_state.current_song_leeh
    st.image(songh7['poster'], width=150)
    st.write(songh7['song_name'])
    if st.button("▶ Play", key="play_eleeh"):
      talk_lee(s_leeh)
      recommand(s_leeh)
# Middle Column - Fixed Song 2
  with mii:
    songh8 = st.session_state.current_song_miih
    st.image(songh8['poster'], width=150)
    st.write(songh8['song_name'])
    if st.button("▶ Play", key="play_emiih"):
      talk_mii(s_miih)
      recommand(s_miih)

# Right Column - "Now Playing" Section
  with rii:
    songh9 = st.session_state.current_song_riih
    st.image(songh9['poster'], width=150)
    st.write(songh9['song_name'])
    if st.button("▶ Play", key="play_eriih"):
      talk_rii(s_riih)
      recommand(s_riih)
# show()
