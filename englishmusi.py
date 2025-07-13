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
  dme=df1[df1['language']=='English']
  import random
  dme=df1[df1['language']=='English']
  if 'songs_eselected' not in st.session_state:
    st.session_state.songs_eselected = random.sample(dme.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_lefte = st.session_state.songs_eselected[0]
    st.session_state.current_song_middlee = st.session_state.songs_eselected[1]
    st.session_state.current_song_righte = st.session_state.songs_eselected[2]
    st.session_state.current_song_lee = st.session_state.songs_eselected[3]
    st.session_state.current_song_mie = st.session_state.songs_eselected[4]
    st.session_state.current_song_rie = st.session_state.songs_eselected[5]
    st.session_state.current_song_leee = st.session_state.songs_eselected[6]
    st.session_state.current_song_miie = st.session_state.songs_eselected[7]
    st.session_state.current_song_riie = st.session_state.songs_eselected[8]
# Layout columns
    lefte, middlee, righte = st.columns(3)
    songe1 = st.session_state.current_song_lefte
    songe2=st.session_state.current_song_middlee
    songe3=st.session_state.current_song_righte
    songe4= st.session_state.current_song_lee 
    songe5= st.session_state.current_song_mie
    songe6= st.session_state.current_song_rie
    songe7=st.session_state.current_song_leee
    songe8=st.session_state.current_song_miie
    songe9=st.session_state.current_song_riie

    s_le=songe1['song_name']
    s_me=songe2['song_name']
    s_re=songe3['song_name']
    s_lee=songe4['song_name']
    s_mie=songe5['song_name']
    s_rie=songe6['song_name']
    s_leee=songe7['song_name']
    s_miie=songe8['song_name']
    s_riie=songe9['song_name']

  def talk_r(s_re):
         engine = pyttsx3.init()
         engine.say(s_re)
         engine.runAndWait()
         def play_songs(s_re):
             if (s_re):
              st.write(f"Playing the song: {s_re}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_re + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_re}"
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
         def play(s_re):
              url = play_songs(s_re)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_re)



  
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  df1['combined_features']=df1['Genre']+df1['language']
  c=cv.fit_transform(df1['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
# similarity
  ds1  = df1.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
  import random
# l, m, r = st.columns(3) 
  def recommand(song_name):
    index=df1[df1['song_name']==song_name].index[0]
    distance1 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    s=[df1.iloc[i[0]] for i in distance1[1:7]]  
    rec = random.sample(s, min(len(s), 7))
    for song in rec: 
     songs = song['song_name']
     poster_url = song['poster']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
  import urllib
  import requests
  def talk_l(s_le):
        engine = pyttsx3.init()
        engine.say(s_le)
        engine.runAndWait()
        def play_songs(s_le):
            if (s_le):
             st.write(f"Playing the song: {s_le}")
            query = urllib.parse.quote(s_le + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_le}"
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
        def play(s_le):
            url = play_songs(s_le)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_le)

  def talk_m(s_me):
        engine = pyttsx3.init()
        engine.say(s_me)
        engine.runAndWait()
        def play_songs(s_me):
            if (s_me):
              st.write(f"Playing the song: {s_me}")
            query = urllib.parse.quote(s_me + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_me}"
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
        def play(s_me):
            url = play_songs(s_me)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_me)
  if 'songs_eselected' not in st.session_state:
    st.session_state.current_song_lefte = st.session_state.songs_eselected[0]
    st.session_state.current_song_middlee = st.session_state.songs_eselected[1]
    st.session_state.current_song_righte = st.session_state.songs_eselected[2]
    st.session_state.current_song_lee = st.session_state.songs_eselected[3]
    st.session_state.current_song_mie = st.session_state.songs_eselected[4]
    st.session_state.current_song_rie = st.session_state.songs_eselected[5]
    st.session_state.current_song_leee = st.session_state.songs_eselected[6]
    st.session_state.current_song_miie = st.session_state.songs_eselected[7]
    st.session_state.current_song_riie = st.session_state.songs_eselected[8]

  songe1 = st.session_state.current_song_lefte
  songe2=st.session_state.current_song_middlee
  songe3=st.session_state.current_song_righte
  songe4= st.session_state.current_song_lee 
  songe5= st.session_state.current_song_mie
  songe6= st.session_state.current_song_rie
  songe7=st.session_state.current_song_leee
  songe8=st.session_state.current_song_miie
  songe9=st.session_state.current_song_riie
  s_le=songe1['song_name']
  s_me=songe2['song_name']
  s_re=songe3['song_name']
  s_lee=songe4['song_name']
  s_mie=songe5['song_name']
  s_rie=songe6['song_name']
  s_leee=songe7['song_name']
  s_miie=songe8['song_name']
  s_riie=songe9['song_name']
  lefte, middlee, righte = st.columns(3)              
  lefte.image(songe1['poster'], width=150)
  with lefte:
    st.write(s_le)
    if st.button("▶ Play", key="play_elefte"):
      talk_l(s_le)
      st.subheader("Made For You:")
      recommand(s_le)   
    
  middlee.image(songe2['poster'], width=150)
  with middlee:
    st.write(s_me)
    if st.button("▶ Play", key="play_emiddlee"):
      talk_m(s_me)     
      recommand(s_me)
  righte.image(songe3['poster'], width=150)
  with righte:
    st.write(s_re)
    if st.button("▶ Play", key="play_erighte"):
     talk_r(s_re)
     recommand(s_re)
  import requests
  def talk_le(s_lee):
        engine = pyttsx3.init()
        engine.say(s_lee)
        engine.runAndWait()
        def play_songs(s_lee):
            if (s_lee):
             st.write(f"Playing the song: {s_lee}")
            query = urllib.parse.quote(s_lee + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lee}"
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              st.write("Please provide a song name.")
              talk_le("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_lee):
            url = play_songs(s_lee)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lee)


  def talk_mi(s_mie):
        engine = pyttsx3.init()
        engine.say(s_mie)
        engine.runAndWait()
        def play_songs(s_mie):
            if (s_mie):
             st.write(f"Playing the song: {s_mie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mie + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mie}"
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
        def play(s_mie):
            url = play_songs(s_mie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mie)
  import urllib
  def talk_ri(s_rie):
        engine = pyttsx3.init()
        engine.say(s_rie)
        engine.runAndWait()
        def play_songs(s_rie):
            if (s_rie):
             st.write(f"Playing the song: {s_rie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rie + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_rie}"
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
        def play(s_rie):
            url = play_songs(s_rie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rie)

# Left Column - Fixed Song. 2nd column
  lee, mie, rie = st.columns(3)
  with lee:
   songe4= st.session_state.current_song_lee
   st.image(songe4['poster'], width=150)
   st.write(songe4['song_name'])
   if st.button("▶ Play", key="play_elee"):
      talk_le(s_lee)
      recommand(s_lee)
  
# Middle Column - Fixed Song 2
  with mie:
    songe5 = st.session_state.current_song_mie
    st.image(songe5['poster'], width=150)
    st.write(songe5['song_name'])
    if st.button("▶ Play", key="play_emie"):
      talk_mi(s_mie)
      recommand(s_mie)
      

# Right Column - "Now Playing" Section
  with rie:
    songe6 = st.session_state.current_song_rie
    st.image(songe6['poster'], width=150)
    st.write(songe6['song_name'])
    if st.button("▶ Play", key="play_erie"):
      talk_ri(s_rie)
      recommand(s_rie)
      
      # 3rd row
  leee, miie, riie = st.columns(3)
  def talk_lee(s_leee):
        engine = pyttsx3.init()
        engine.say(s_leee)
        engine.runAndWait()
        def play_songs(s_leee):
            if (s_leee):
             st.write(f"Playing the song: {s_leee}")
            query = urllib.parse.quote(s_leee + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_leee}"
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
        def play(s_leee):
            url = play_songs(s_leee)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_leee)
  def talk_mii(s_miie):
        engine = pyttsx3.init()
        engine.say(s_miie)
        engine.runAndWait()
        def play_songs(s_miie):
            if (s_miie):
             st.write(f"Playing the song: {s_miie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miie + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_miie}"
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
        def play(s_miie):
            url = play_songs(s_miie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_miie)
  def talk_rii(s_riie):
        engine = pyttsx3.init()
        engine.say(s_riie)
        engine.runAndWait()
        def play_songs(s_riie):
            if (s_riie):
             st.write(f"Playing the song: {s_riie}")
            
            
            query = urllib.parse.quote(s_riie + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_riie}"
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
        def play(s_riie):
            url = play_songs(s_riie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_riie)
# Left Column - Fixed Song 1
  with leee:
    songe7= st.session_state.current_song_leee
    st.image(songe7['poster'], width=150)
    st.write(songe7['song_name'])
    if st.button("▶ Play", key="play_eleee"):
      talk_lee(s_leee)
      recommand(s_leee)
# Middle Column - Fixed Song 2
  with miie:
    songe8 = st.session_state.current_song_miie
    st.image(songe8['poster'], width=150)
    st.write(songe8['song_name'])
    if st.button("▶ Play", key="play_emiih"):
      talk_mii(s_miie)
      recommand(s_miie)

# Right Column - "Now Playing" Section
  with riie:
    songe9 = st.session_state.current_song_riie
    st.image(songe9['poster'], width=150)
    st.write(songe9['song_name'])
    if st.button("▶ Play", key="play_eriih"):
      talk_rii(s_riie)
      recommand(s_riie)
# show()
