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
df=pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
df5=pd.read_csv('hindimov.csv',encoding='ISO-8859-1')


movies=df

# df1=pd.read_csv("series_data.csv")
# option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'])

# if option=='Music':
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
  search_query = st.text_input("Search for a movie")
  if search_query:
   if len(search_query) >= 3:
    fil_df=df5[df5.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
    if not fil_df.empty:
     st.subheader("Search Results:")
     if len(fil_df)==1:
    #  st.write(fil_df)
      img=fil_df['poster_path'].iloc[0]
    #  img1=fil_df['poster'].iloc[1]
# st.columns
      # with left:
      st.image(img,width=200)
    #  st.image(img1,width=200)
      s=fil_df['poster_path'].iloc[0]
      import requests
      import urllib
      def talk_l(s):
         engine = pyttsx3.init()
         engine.say(s)
         engine.runAndWait()
      def play_songs(s):
             if (s):
              st.write(f"Playing the trailer: {s}")
              
              query = urllib.parse.quote(s + " official trailer")
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
                st.write("Please provide a movie name.")
                talk_l("Please provide a movie name.")
        #  play_songs(s_l)
      def play(s):
              url = play_songs(s)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this movie 😢")
      
      if st.button("▶ Play"):
         talk_l(s)
         play_songs(s)
         play(s)
    #  s1=fil_df['song_name'].iloc[1]
      st.write(s)
    #  st.write(s1)
     else: 
      lef, mid = st.columns(2)
      img1=fil_df['poster_path'].iloc[0]
      img2=fil_df['poster_path'].iloc[1]
      
      
      s1=fil_df['Title'].iloc[0]
      s2=fil_df['Title'].iloc[1]
      import requests
      import urllib
      def talk_l(s1):
         engine = pyttsx3.init()
         engine.say(s1)
         engine.runAndWait()
      def play_songs(s1):
             if (s1):
              st.write(f"Playing the movie: {s1}")
              
              query = urllib.parse.quote(s1 + " official trailer")
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
                st.write("Please provide a movie name.")
                talk_l("Please provide a movie name.")
      def play(s1):
              url = play_songs(s1)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this movie 😢")
      def talk_m(s2):
         engine = pyttsx3.init()
         engine.say(s2)
         engine.runAndWait()
         def play_songs(s2):
             if (s2):
              st.write(f"Playing the movie: {s2}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s2 + "official trailer")
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
                st.write("Please provide a movie name.")
                talk_m("Please provide a movie name.")
        #  play_songs(s_l)
             def play(s2):
              url = play_songs(s2)
              if url:
                st.markdown(
                   f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this movie 😢")
             play(s2)
      lef.image(img1,width=200)
      with lef:
       st.write(s1)
       if st.button("▶ Play",key="re_lef"):
        talk_l(s1)
        play_songs(s1)
        play(s1)
      
      mid.image(img2,width=200)
      with mid:
       st.write(s2)
       if st.button("▶ Play",key="re_mid"):
        talk_m(s2)
        play_songs(s2)
        play(s2)
    else:
     st.write("Movie does not exist")
  else:
   st.write("")
  # dmh=df5[df5['original_language']=='Hindi']
  import random
  # dmh=df5[df5['original_language']=='Hindi']
  if 'songs_selectedh' not in st.session_state:
    st.session_state.songs_selectedh = random.sample(df5.to_dict('records'), 9) # Pick 2 random songs
    st.session_state.current_song_lefthm = st.session_state.songs_selectedh[0]
    st.session_state.current_song_middlehm = st.session_state.songs_selectedh[1]
    st.session_state.current_song_righthm = st.session_state.songs_selectedh[2]
    st.session_state.current_song_lehm = st.session_state.songs_selectedh[3]
    st.session_state.current_song_mihm = st.session_state.songs_selectedh[4]
    st.session_state.current_song_rihm = st.session_state.songs_selectedh[5]
    st.session_state.current_song_leehm = st.session_state.songs_selectedh[6]
    st.session_state.current_song_miihm = st.session_state.songs_selectedh[7]
    st.session_state.current_song_riihm = st.session_state.songs_selectedh[8]
# Layout columns
    lefthm, middlehm, righthm = st.columns(3)
    songhm1 = st.session_state.current_song_lefthm
    songhm2=st.session_state.current_song_middlehm
    songhm3=st.session_state.current_song_righthm
    songhm4= st.session_state.current_song_lehm
    songhm5= st.session_state.current_song_mihm
    songhm6= st.session_state.current_song_rihm
    songhm7=st.session_state.current_song_leehm
    songhm8=st.session_state.current_song_miihm
    songhm9=st.session_state.current_song_riihm

    s_lhm=songhm1['Title']
    s_mhm=songhm2['Title']
    s_rhm=songhm3['Title']
    s_lehm=songhm4['Title']
    s_mihm=songhm5['Title']
    s_rihm=songhm6['Title']
    s_leehm=songhm7['Title']
    s_miihm=songhm8['Title']
    s_riihm=songhm9['Title']

  def talk_r(s_rhm):                    
        engine = pyttsx3.init()
        engine.say(s_rhm)
        engine.runAndWait()
        def play_songs(s_rhm):
             if (s_rhm):
              st.write(f"Playing the trailer: {s_rhm}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
             query = urllib.parse.quote(s_rhm + " official trailer")
             url=f"https://www.youtube.com/results?search_query={s_rhm}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}") 
             response = requests.get(url)
             video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
             if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
             else:
               return None
              
            # else:
            #     st.write("Please provide a movie name.")
            #     talk_r("Please provide a movie name.")
        #  play_songs(s_l)
        def play(s_rhm):
              url = play_songs(s_rhm)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this movie 😢")
        play(s_rhm)

  from sklearn.feature_extraction.text import CountVectorizer
  cv5=CountVectorizer(max_features=10000, stop_words='english')
  df5['combined_features']=df5['genres']+df5['original_language']
  c5=cv5.fit_transform(df5['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c5)
# similarity
  # ds5  = df5.drop(columns=['genres','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
  import random
# l, m, r = st.columns(3) 
  def recommandh(song_name):
    index=df5[df5['Title']==song_name].index[0]
    distance5 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
   
    s5=[df5.iloc[i[0]] for i in distance5[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s5, min(len(s5), 7))
    for song in rec: 
#  st.write(s1)
     songs = song['Title']
     poster_url = song['poster_path']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
  import requests
  import urllib
  def talk_l(s_lhm):
        engine = pyttsx3.init()
        engine.say(s_lhm)
        engine.runAndWait()
        def play_songs(s_lhm):
            if (s_lhm):
             st.write(f"Playing the song: {s_lhm}")
            
            query = urllib.parse.quote(s_lhm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_lhm}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_lhm):
            url = play_songs(s_lhm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lhm)

  def talk_m(s_mhm):
        engine = pyttsx3.init()
        engine.say(s_mhm)
        engine.runAndWait()
        def play_songs(s_mhm):
            if (s_mhm):
              st.write(f"Playing the song: {s_mhm}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mhm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_mhm}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            
            else:
              st.write("Please provide a movie name.")
              talk_m("Please provide a movie name.")
      #  play_songs(s_l)
        def play(s_mhm):
            url = play_songs(s_mhm)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_mhm)
# recommand(s_l)      
# 1st column
  songhm1 = st.session_state.current_song_lefthm
  songhm2=st.session_state.current_song_middlehm
  songhm3=st.session_state.current_song_righthm
  songhm4= st.session_state.current_song_lehm
  songhm5= st.session_state.current_song_mihm
  songhm6= st.session_state.current_song_rihm
  songhm7=st.session_state.current_song_leehm
  songhm8=st.session_state.current_song_miihm
  songhm9=st.session_state.current_song_riihm
  s_lhm=songhm1['Title']
  s_mhm=songhm2['Title']
  s_rhm=songhm3['Title']
  s_lehm=songhm4['Title']
  s_mihm=songhm5['Title']
  s_rihm=songhm6['Title']
  s_leehm=songhm7['Title']
  s_miihm=songhm8['Title']
  s_riihm=songhm9['Title']
  lefthmm, middlehmm, righthmm = st.columns(3)              
  lefthmm.image(songhm1['poster_path'], width=150)
  with lefthmm:
   st.write(s_lhm)
   if st.button("▶ Play", key="play_left"):
  # v=s_l
    talk_l(s_lhm)
#  if st.button("Recommend", key="rec_left"):
    st.subheader("Made For You:")
    recommandh(s_lhm)   #recommnded songs for left
    
  middlehmm.image(songhm2['poster_path'], width=150)
  with middlehmm:
    st.write(s_mhm)
    if st.button("▶ Play", key="play_middle"):
  # v=s_l
     talk_m(s_mhm)     
     recommandh(s_mhm)
# if st.button("Recommend", key="rec_middle")  
  righthmm.image(songhm3['poster_path'], width=150)
  with righthmm:
    st.write(s_rhm)
    if st.button("▶ Play", key="play_right"):
  # v=s_l
      talk_r(s_rhm)
  

      recommandh(s_rhm)
  
# 2 layout columns 
  import requests
  def talk_le(s_lehm):
        engine = pyttsx3.init()
        engine.say(s_lehm)
        engine.runAndWait()
        def play_songs(s_lehm):
            if (s_lehm):
             st.write(f"Playing the song: {s_lehm}")
            query = urllib.parse.quote(s_lehm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_lehm}"
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
              talk_le("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_lehm):
            url = play_songs(s_lehm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lehm)


  def talk_mi(s_mihm):
        engine = pyttsx3.init()
        engine.say(s_mihm)
        engine.runAndWait()
        def play_songs(s_mihm):
            if (s_mihm):
             st.write(f"Playing the movie: {s_mihm}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mihm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_mihm}"
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
        def play(s_mihm):
            url = play_songs(s_mihm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mihm)
  import urllib
  def talk_ri(s_rihm):
        engine = pyttsx3.init()
        engine.say(s_rihm)
        engine.runAndWait()
        def play_songs(s_rihm):
            if (s_rihm):
             st.write(f"Playing the song: {s_rihm}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rihm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_rihm}"
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
        def play(s_rihm):
            url = play_songs(s_rihm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rihm)

# Left Column - Fixed Song. 2nd column
  lehhm, mihhm, rihhm = st.columns(3)
  with lehhm:
    songhm4= st.session_state.current_song_lehm
    st.image(songhm4['poster_path'], width=150)
    st.write(songhm4['Title'])
    if st.button("▶ Play", key="play_le"):
      talk_le(s_lehm)
      recommandh(s_lehm)
  
# Middle Column - Fixed Song 2
  with mihhm:
    songhm5 = st.session_state.current_song_mihm
    st.image(songhm5['poster_path'], width=150)
    st.write(songhm5['Title'])
    if st.button("▶ Play", key="play_mi"):
      talk_mi(s_mihm)
      recommandh(s_mihm)
      

# Right Column - "Now Playing" Section
  with rihhm:
    songhm6 = st.session_state.current_song_rihm
    st.image(songhm6['poster_path'], width=150)
    st.write(songhm6['Title'])
    if st.button("▶ Play", key="play_ri"):
      talk_ri(s_rihm)
      recommandh(s_rihm)
      
      # 3rd row
  leehhm, miihhm, riihhm = st.columns(3)
  def talk_lee(s_leehm):
        engine = pyttsx3.init()
        engine.say(s_leehm)
        engine.runAndWait()
        def play_songs(s_leehm):
            if (s_leehm):
             st.write(f"Playing the song: {s_leehm}")
            
            
            query = urllib.parse.quote(s_leehm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_leehm}"
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
        def play(s_leehm):
            url = play_songs(s_leehm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_leehm)
  def talk_mii(s_miihm):
        engine = pyttsx3.init()
        engine.say(s_miihm)
        engine.runAndWait()
        def play_songs(s_miihm):
            if (s_miihm):
             st.write(f"Playing the song: {s_miihm}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miihm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_miihm}"
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
        def play(s_miihm):
            url = play_songs(s_miihm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_miihm)
  def talk_rii(s_riihm):
        engine = pyttsx3.init()
        engine.say(s_riihm)
        engine.runAndWait()
        def play_songs(s_riihm):
            if (s_riihm):
             st.write(f"Playing the song: {s_riihm}")
            
            
            query = urllib.parse.quote(s_riihm + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_riihm}"
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
        def play(s_riihm):
            url = play_songs(s_riihm)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_riihm)
# Left Column - Fixed Song 1
  with leehhm:
    songh7= st.session_state.current_song_leehm
    st.image(songh7['poster_path'], width=150)
    st.write(songh7['Title'])
    if st.button("▶ Play", key="play_lee"):
      talk_lee(s_leehm)
      recommandh(s_leehm)
# Middle Column - Fixed Song 2
  with miihhm:
    songh8 = st.session_state.current_song_miihm
    st.image(songh8['poster_path'], width=150)
    st.write(songh8['Title'])
    if st.button("▶ Play", key="play_mii"):
      talk_mii(s_miihm)
      recommandh(s_miihm)

# Right Column - "Now Playing" Section
  with riihhm:
    songhm9 = st.session_state.current_song_riihm
    st.image(songhm9['poster_path'], width=150)
    st.write(songhm9['Title'])
    if st.button("▶ Play", key="play_rii"):
      talk_rii(s_riihm)
      recommandh(s_riihm)
# show()
