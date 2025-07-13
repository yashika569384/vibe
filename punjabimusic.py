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
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from sklearn.metrics.pairwise import cosine_similarity
# st.set_page_config(page_title='VibeVistanew')
# st.title(":red[VibeVista:microphone:]")
# df1 = pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
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
  songs=df
# df1=pd.read_csv("series_data.csv")
# option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'])
  search_query = st.text_input("Search for a song")


  if search_query:
   if len(search_query) >= 3:
    fil_df=df[df.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
    if not fil_df.empty:
     st.subheader("Search Results:")
     if len(fil_df)==1:
    #  st.write(fil_df)
      img=fil_df['poster'].iloc[0]
    #  img1=fil_df['poster'].iloc[1]
# st.columns
      # with left:
      st.image(img,width=200)
    #  st.image(img1,width=200)
      s=fil_df['song_name'].iloc[0]
      import requests
      import urllib
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
    #  s1=fil_df['song_name'].iloc[1]
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
       if st.button("▶ Play",key="re_lefp"):
        talk_l(s1)
        play_songs(s1)
        play(s1)
      
      mid.image(img2,width=200)
      with mid:
       st.write(s2)
       if st.button("▶ Play",key="re_midp"):
        talk_m(s2)
        play_songs(s2)
        play(s2)
    else:
     st.write("Song does not exist")
  else:
   st.write("")

# if l=='Punjabi':
  dmp=df3[df3['language']=='Punjabi']
  import random
  dmp=df3[df3['language']=='Punjabi']
  if 'songs_pselected' not in st.session_state:
    st.session_state.songs_pselected = random.sample(dmp.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_leftp = st.session_state.songs_pselected[0]
    st.session_state.current_song_middlep = st.session_state.songs_pselected[1]
    st.session_state.current_song_rightp = st.session_state.songs_pselected[2]
    st.session_state.current_song_lep = st.session_state.songs_pselected[3]
    st.session_state.current_song_mip = st.session_state.songs_pselected[4]
    st.session_state.current_song_rip = st.session_state.songs_pselected[5]
    st.session_state.current_song_leep = st.session_state.songs_pselected[6]
    st.session_state.current_song_miip = st.session_state.songs_pselected[7]
    st.session_state.current_song_riip = st.session_state.songs_pselected[8]
# Layout columns
    leftp, middlep, rightp = st.columns(3)
    songp1 = st.session_state.current_song_leftp
    songp2=st.session_state.current_song_middlep
    songp3=st.session_state.current_song_rightp
    songp4= st.session_state.current_song_lep 
    songp5= st.session_state.current_song_mip
    songp6= st.session_state.current_song_rip
    songp7=st.session_state.current_song_leep
    songp8=st.session_state.current_song_miip
    songp9=st.session_state.current_song_riip

    s_lp=songp1['song_name']
    s_mp=songp2['song_name']
    s_rp=songp3['song_name']
    s_lep=songp4['song_name']
    s_mip=songp5['song_name']
    s_rip=songp6['song_name']
    s_leep=songp7['song_name']
    s_miip=songp8['song_name']
    s_riip=songp9['song_name']

  def talk_r(s_rp):
         engine = pyttsx3.init()
         engine.say(s_rp)
         engine.runAndWait()
         def play_songs(s_rp):
             if (s_rp):
              st.write(f"Playing the song: {s_rp}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_rp + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_rp}"
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
         def play(s_rp):
              url = play_songs(s_rp)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_rp)



  

  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  df3['combined_features']=df3['Genre']+df3['language']
  c3=cv.fit_transform(df3['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c3)
# similarity
  ds3  = df3.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
  import random
# l, m, r = st.columns(3) 
  def recommandp(song_name):
    index=df3[df3['song_name']==song_name].index[0]
    distance3 = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    
    s3=[df3.iloc[i[0]] for i in distance3[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s3, min(len(s3), 7))
    for song in rec: 
#  st.write(s1)
     songs = song['song_name']
     poster_url = song['poster']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(songs)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
  import urllib
  import requests
  def talk_l(s_lp):
        engine = pyttsx3.init()
        engine.say(s_lp)
        engine.runAndWait()
        def play_songs(s_lp):
            if (s_lp):
             st.write(f"Playing the song: {s_lp}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_lp + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lp}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_lp):
            url = play_songs(s_lp)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lp)

  def talk_m(s_mp):
        engine = pyttsx3.init()
        engine.say(s_mp)
        engine.runAndWait()
        def play_songs(s_mp):
            if (s_mp):
              st.write(f"Playing the song: {s_mp}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mp + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mp}"
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
        def play(s_mp):
            url = play_songs(s_mp)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mp)
# recommand(s_l)      
# 1st column
  songp1 = st.session_state.current_song_leftp
  songp2=st.session_state.current_song_middlep
  songp3=st.session_state.current_song_rightp
  songp4= st.session_state.current_song_lep   
  songp5= st.session_state.current_song_mip
  songp6= st.session_state.current_song_rip
  songp7=st.session_state.current_song_leep
  songp8=st.session_state.current_song_miip
  songp9=st.session_state.current_song_riip
  s_lp=songp1['song_name']
  s_mp=songp2['song_name']  
  s_rp=songp3['song_name']
  s_lep=songp4['song_name']
  s_mip=songp5['song_name'] 
  s_rip=songp6['song_name'] 
  s_leep=songp7['song_name']
  s_miip=songp8['song_name']
  s_riip=songp9['song_name']
  leftp, middlep, rightp = st.columns(3)              
  leftp.image(songp1['poster'], width=150)
  with leftp:
    st.write(s_lp)
    if st.button("▶ Play", key="play_pleftp"):
  # v=s_l
     talk_l(s_lp)
#  if st.button("Recommend", key="rec_left"):
     st.subheader("Made For You:")
     recommandp(s_lp)   #recommnded songs for left
    
  middlep.image(songp2['poster'], width=150)
  with middlep:
   st.write(s_mp)
   if st.button("▶ Play", key="play_pmiddlep"):
  # v=s_l
      talk_m(s_mp)     
      recommandp(s_mp)
# if st.button("Recommend", key="rec_middle")  
  rightp.image(songp3['poster'], width=150)
  with rightp:
    st.write(s_rp)
    if st.button("▶ Play", key="play_prightp"):
  # v=s_l
      talk_r(s_rp)
      recommandp(s_rp)
  
# 2 layout columns 
  import requests
  def talk_le(s_lep):
        engine = pyttsx3.init()
        engine.say(s_lep)
        engine.runAndWait()
        def play_songs(s_lep):
            if (s_lep):
             st.write(f"Playing the song: {s_lep}")
            query = urllib.parse.quote(s_lep + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lep}"
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
        def play(s_lep):
            url = play_songs(s_lep)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_lep)


  def talk_mi(s_mip):
        engine = pyttsx3.init()
        engine.say(s_mip)
        engine.runAndWait()
        def play_songs(s_mip):
            if (s_mip):
             st.write(f"Playing the song: {s_mip}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mip + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mip}"
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
        def play(s_mip):
            url = play_songs(s_mip)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mip)
  import urllib
  def talk_ri(s_rip):
        engine = pyttsx3.init()
        engine.say(s_rip)
        engine.runAndWait()
        def play_songs(s_rip):
            if (s_rip):
             st.write(f"Playing the song: {s_rip}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rip + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_rip}"
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
        def play(s_rip):
            url = play_songs(s_rip)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rip)

# Left Column - Fixed Song. 2nd column
  lepp, mipp, ripp = st.columns(3)
  with lepp:
    songp4= st.session_state.current_song_lep
    st.image(songp4['poster'], width=150)
    st.write(songp4['song_name'])
    if st.button("▶ Play", key="play_plep"):
      talk_le(s_lep)
      recommandp(s_lep)
  
# Middle Column - Fixed Song 2
  with mipp:
    songp5 = st.session_state.current_song_mip
    st.image(songp5['poster'], width=150)
    st.write(songp5['song_name'])
    if st.button("▶ Play", key="play_pmip"):
      talk_mi(s_mip)
      recommandp(s_mip)
      

# Right Column - "Now Playing" Section
  with ripp:
    songp6 = st.session_state.current_song_rip
    st.image(songp6['poster'], width=150)
    st.write(songp6['song_name'])
    if st.button("▶ Play", key="play_prip"):
      talk_ri(s_rip)
      recommandp(s_rip)
      
      # 3rd row
  leep, miip, riip = st.columns(3)
  def talk_lee(s_leep):
        engine = pyttsx3.init()
        engine.say(s_leep)
        engine.runAndWait()
        def play_songs(s_leep):
            if (s_leep):
             st.write(f"Playing the song: {s_leep}")
            query = urllib.parse.quote(s_leep + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_leep}"
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
        def play(s_leep):
            url = play_songs(s_leep)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_leep)
  def talk_mii(s_miip):
        engine = pyttsx3.init()
        engine.say(s_miip)
        engine.runAndWait()
        def play_songs(s_miip):
            if (s_miip):
             st.write(f"Playing the song: {s_miip}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miip + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_miip}"
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
        def play(s_miip):
            url = play_songs(s_miip)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_miip)
  def talk_rii(s_riip):
        engine = pyttsx3.init()
        engine.say(s_riip)
        engine.runAndWait()
        def play_songs(s_riip):
            if (s_riip):
             st.write(f"Playing the song: {s_riip}")
            
            
            query = urllib.parse.quote(s_riip + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_riip}"
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
        def play(s_riip):
            url = play_songs(s_riip)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_riip)
# Left Column - Fixed Song 1
  with leep:
    songp7= st.session_state.current_song_leep
    st.image(songp7['poster'], width=150)
    st.write(songp7['song_name'])
    if st.button("▶ Play", key="play_pleep"):
      talk_lee(s_leep)
      recommandp(s_leep)
# Middle Column - Fixed Song 2
  with miip:
    songp8 = st.session_state.current_song_miip
    st.image(songp8['poster'], width=150)
    st.write(songp8['song_name'])
    if st.button("▶ Play", key="play_pmiip"):
      talk_mii(s_miip)
      recommandp(s_miip)

# Right Column - "Now Playing" Section
  with riip:
    songp9 = st.session_state.current_song_riip
    st.image(songp9['poster'], width=150)
    st.write(songp9['song_name'])
    if st.button("▶ Play", key="play_priip"):
      talk_rii(s_riip)
      recommandp(s_riip)

  