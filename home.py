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
import hindimusic
import englishmusic
import punjabimusic
import hindimovie
import punjabimovie
import englishmovie
import kdrama
import random


# st.set_page_config(page_title='VibeVista')
st.title(":red[VibeVerse:microphone:]")
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
df1=pd.read_csv('englishmusic.csv',encoding='ISO-8859-1')
df2=pd.read_csv('hindimusic.csv',encoding='ISO-8859-1')
df3=pd.read_csv('punjabimusic.csv',encoding='ISO-8859-1')
dfm=pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
dfk=pd.read_csv('kdrama1 final.csv',encoding='ISO-8859-1')

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
          width: 150px;
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
  # if 'songs_musselected' not in st.session_state:
  #   st.session_state.songs_musselected = random.sample(df.to_dict('records'), 3)
  #   st.session_state.current_song_leftmus = st.session_state.songs_musselected[0]
  #   st.session_state.current_song_middlemus = st.session_state.songs_musselected[1]
  #   st.session_state.current_song_rightmus = st.session_state.songs_musselected[2]
  #   songmu1=st.session_state.current_song_leftmus
  #   songmu2=st.session_state.current_song_middlemus
  #   songmu3=st.session_state.current_song_rightmus
    
  
    
  # if 'songs_mselected' not in st.session_state:
  #   st.session_state.songs_mselected = random.sample(dfm.to_dict('records'), 3)
  #   st.session_state.current_song_leftm = st.session_state.songs_mselected[0]
  #   st.session_state.current_song_middlem = st.session_state.songs_mselected[1]
  #   st.session_state.current_song_rightm = st.session_state.songs_mselected[2]
  #   m1=st.session_state.current_song_leftm
  #   m2=st.session_state.current_song_middlem
  #   m3=st.session_state.current_song_rightm    

  # if 'songs_kdselected' not in st.session_state:
  #   st.session_state.songs_kdselected = random.sample(dfk.to_dict('records'), 3)
  #   st.session_state.current_song_leftkd = st.session_state.songs_kdselected[0]
  #   st.session_state.current_song_middlekd = st.session_state.songs_kdselected[1]
  #   st.session_state.current_song_rightkd = st.session_state.songs_kdselected[2]
  #   k1=st.session_state.current_song_leftkd
  #   k2=st.session_state.current_song_middlekd
  #   k3=st.session_state.current_song_rightkd

   
  #   s_lmu=songmu1['song_name']
  #   s_mmu=songmu2['song_name']
  #   s_rmu=songmu3['song_name']


  #   s_lm=m1['Title']
  #   s_mm=m2['Title']
  #   s_rm=m3['Title']

  #   s_lk=k1['Name']
  #   s_mk=k2['Name']
  #   s_rk=k3['Name']
# if 'songs_musselected' not in st.session_state:
#     st.session_state.songs_musselected = random.sample(df.to_dict('records'), 3)  # Pick 2 random songs
#     st.session_state.current_song_leftmus = st.session_state.songs_musselected[0]
#     st.session_state.current_song_middlemus = st.session_state.songs_musselected[1]
#     st.session_state.current_song_rightmus = st.session_state.songs_musselected[2]
    
#   # left, middle, right = st.columns(3)
# songmu1 = st.session_state.current_song_leftmus
# songmu2 = st.session_state.current_song_middlemus
# songmu3 = st.session_state.current_song_rightmus

# s_lmu = songmu1['song_name']
# s_mmu = songmu2['song_name']
# s_rmu = songmu3['song_name']

# # 🛑 Function should be OUTSIDE


# def talk_l(s_lmu):
#         engine = pyttsx3.init()
#         engine.say(s_lmu)
#         engine.runAndWait()
#         def play_songs(s_lmu):
#             if (s_lmu):
#              st.write(f"Playing the song: {s_lmu}")
#             query = urllib.parse.quote(s_lmu + " official audio")
#             url=f"https://www.youtube.com/results?search_query={s_lmu}"
#             response = requests.get(url)
#             video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
#             if video_ids:
#               return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
#             else:
#               return None
#         def play(s_lmu):
#               url = play_songs(s_lmu)
#               if url:
#                 st.markdown(
#                     f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                   )
#               else:
#                   st.error("No video found for this song 😢")
#         play(s_lmu)

# def talk_m(s_mmu):
#          engine = pyttsx3.init()
#          engine.say(s_mmu)
#          engine.runAndWait()
#          def play_songs(s_mmu):
#              if (s_mmu):
#               st.write(f"Playing the song: {s_mmu}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_mmu + " official audio")
#               url=f"https://www.youtube.com/results?search_query={s_mmu}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a song name.")
#                 talk_m("Please provide a song name.")
#         #  play_songs(s_l)
#          def play(s_mmu):
#               url = play_songs(s_mmu)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this song 😢")
#          play(s_mmu)

# def talk_r(s_rmu):
#          engine = pyttsx3.init()
#          engine.say(s_rmu)
#          engine.runAndWait()
#          def play_songs(s_rmu):
#              if (s_rmu):
#               st.write(f"Playing the song: {s_rmu}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_rmu + " official audio")
#               url=f"https://www.youtube.com/results?search_query={s_rmu}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a song name.")
#                 talk_m("Please provide a song name.")
#         #  play_songs(s_l)
#          def play(s_rmu):
#               url = play_songs(s_rmu)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this song 😢")
#          play(s_rmu)
# # st.set_page_config(page_title="Music Selector", layout="wide")
# # movie
# def talk_lm(s_lm):
#          engine = pyttsx3.init()
#          engine.say(s_lm)
#          engine.runAndWait()
#          def play_songs(s_lm):
#              if (s_lm):
#               st.write(f"Playing the trailer: {s_lm}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_lm + " official trailer")
#               url=f"https://www.youtube.com/results?search_query={s_lm}"
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a movie name.")
#                 talk_lm("Please provide a movie name.")
#         #  play_songs(s_l)
#          def play(s_lm):
#               url = play_songs(s_lm)
#               if url:
#                 st.markdown(
#                    f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this movie 😢")
#          play(s_lm)

# def talk_mm(s_mm):
#          engine = pyttsx3.init()
#          engine.say(s_mm)
#          engine.runAndWait()
#          def play_songs(s_mm):
#              if (s_mm):
#               st.write(f"Playing the trailer: {s_mm}")  
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_mm + " official trailer")
#               url=f"https://www.youtube.com/results?search_query={s_mm}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a movie name.")
#                 talk_mm("Please provide a movie name.")
#         #  play_songs(s_l)
#          def play(s_mm):
#               url = play_songs(s_mm)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this movie 😢")
#          play(s_mm)

# def talk_rm(s_rm):
#          engine = pyttsx3.init()
#          engine.say(s_rm)
#          engine.runAndWait()
#          def play_songs(s_rm):
#              if (s_rm):
#               st.write(f"Playing the trailer: {s_rm}") 
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_rm + " official trailer")
#               url=f"https://www.youtube.com/results?search_query={s_rm}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
      
#              else:
#                 st.write("Please provide a movie name.")
#                 talk_rm("Please provide a movie name.")
#         #  play_songs(s_l)
#          def play(s_rm):
#               url = play_songs(s_rm)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this movie 😢")
#          play(s_rm)
# #kdrama
# def talk_lk(s_lk):
#          engine = pyttsx3.init()
#          engine.say(s_lk)
#          engine.runAndWait()
#          def play_songs(s_lk):
#              if (s_lk):
#               st.write(f"Playing the song: {s_lk}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_lk + " official audio")
#               url=f"https://www.youtube.com/results?search_query={s_lk}"
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a song name.")
#                 talk_lk("Please provide a song name.")
#         #  play_songs(s_l)
#          def play(s_lk):
#               url = play_songs(s_lk)
#               if url:
#                 st.markdown(
#                    f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this K-Drama 😢")
#          play(s_lk)

# def talk_mk(s_mk):
#          engine = pyttsx3.init()
#          engine.say(s_mk)
#          engine.runAndWait()
#          def play_songs(s_mk):
#              if (s_mk):
#               st.write(f"Playing the trailer: {s_mk}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_mk + " official trailer")
#               url=f"https://www.youtube.com/results?search_query={s_mk}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a K-Drama name.")
#                 talk_m("Please provide a K-Drama name.")
#         #  play_songs(s_l)
#          def play(s_mk):
#               url = play_songs(s_mk)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this K-Drama 😢")
#          play(s_mk)   
# def talk_rk(s_rk):
#          engine = pyttsx3.init()
#          engine.say(s_rk)
#          engine.runAndWait()
#          def play_songs(s_rk):
#              if (s_rk):
#               st.write(f"Playing the song: {s_rk}")
              
#               # talk_l(f"Playing the song {(song1[''])}")
#         # url = f"https://www.google.com/search?q={podcast_name}"
#               query = urllib.parse.quote(s_rk + " official trailer")
#               url=f"https://www.youtube.com/results?search_query={s_rk}"
#             #   webbrowser.open(url)
#             #   print(f"Playing song: {s_l}")
#               response = requests.get(url)
#               video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
#               if video_ids:
#                return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
#               else:
#                return None
              
#              else:
#                 st.write("Please provide a K-Drama name.")
#                 talk_rk("Please provide a K-Drama name.")
#         #  play_songs(s_l)
#          def play(s_rk):
#               url = play_songs(s_rk)
#               if url:
#                 st.markdown(
#                    f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
#             unsafe_allow_html=True,
#                  )
#               else:
#                  st.error("No video found for this K-Drama 😢")
#          play(s_rk)

def show():

  if "page" not in st.session_state:
        st.session_state.page = "Home"
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
    #  if st.button("▶ Play",key='play_left'):
    #       talk_l(song)
          #  play_songs(s)
          # #  play(s)
          # st.write(song)
# 2nd song
    s2=df.sample(n=1)
    song1=s2["song_name"].iloc[0]  
    poster1=s2['poster'].iloc[0]
    middle.image(poster1,width=150)
    with middle:
     st.write(song1)
    #  if st.button("▶ Play",key='play_middle'):
    #       talk_l(song1)
    #       #  play_songs(s)
    #       #  play(s)
    #       st.write(song1)
    # 3rd song
    s3=df.sample(n=1)
    song2=s3["song_name"].iloc[0]
    poster2=s3['poster'].iloc[0]
    right.image(poster2,width=150)
    with right:
      st.write(song2)
      # if st.button("▶ Play",key='play_right'):
      #     talk_l(song2)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(song2)

  #  movies
    df2=pd.read_csv("movieorig.csv",encoding='ISO-8859-1')
    st.header("Movies For You",divider='green')
    leftm, middlem, rightm = st.columns(3, vertical_alignment='center')
    # 1st movie
    m1=df2.sample(n=1)
    mo=m1["Title"].iloc[0]
    mposter=m1['poster_path'].iloc[0]
    leftm.image(mposter,width=150)
    with leftm:
      st.write(mo)
      # if st.button("▶ Play",key='play_leftm'):
      #     talk_lm(mo)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(mo)
  # 2nd song
    m2=df2.sample(n=1)
    mmo=m2["Title"].iloc[0]
    mmposter=m2['poster_path'].iloc[0]
    middlem.image(mmposter,width=150)
    with middlem:
      st.write(mmo)
      # if st.button("▶ Play",key='play_middlem'):
      #     talk_mm(mmo)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(mmo)
      # 3rd song
    m3=df2.sample(n=1)
    mmmo2=m3["Title"].iloc[0]
    mmmposter2=m3['poster_path'].iloc[0]
    rightm.image(mmmposter2,width=150)
    with rightm:
      st.write(mmmo2)
      # if st.button("▶ Play",key='play_rightmt'):
      #     talk_rm(mmmo2)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(mmmo2)

    st.header("K-Drama For You",divider='green')
    leftk, middlek, rightk = st.columns(3, vertical_alignment='center')
  # kdrama
    kdra1=dfk.sample(n=1)
    kdr=kdra1["Name"].iloc[0]
    kdraposter1=kdra1['Poster Path'].iloc[0]
    leftk.image(kdraposter1,width=150)
    with leftk:
      st.write(kdr)
      # if st.button("▶ Play",key='play_leftk'):
      #     talk_lk(kdr)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(kdr)
  # 2nd song
    kdra2=dfk.sample(n=1)
    kdr2=kdra2["Name"].iloc[0]
    kdraposter2=kdra2['Poster Path'].iloc[0]
    middlek.image(kdraposter2,width=150)
    with middlek:
      st.write(kdr2)
      # if st.button("▶ Play",key='play_middlek'):
      #     talk_mk(kdr2)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(kdr2)
    # 3rd song
    kdra3=dfk.sample(n=1)
    kdr3=kdra3["Name"].iloc[0]
    kdraposter3=kdra3['Poster Path'].iloc[0]
    rightk.image(kdraposter3,width=150)
    with rightk:
      st.write(kdr3)
      # if st.button("▶ Play",key='play_rightk'):
      #     talk_rk(kdr3)
      #     #  play_songs(s)
      #     #  play(s)
      #     st.write(kdr3)

  elif option == 'Music':
      st.session_state.page = "Music"
  elif option == 'Movies':
      st.session_state.page = "Movies"
  elif option == 'K-Drama':
      st.session_state.page = "kdrama"
  else:
      st.write("")
    

  if st.session_state.page == "Music":
        music.show()
  elif st.session_state.page == "Movies":
        movie.show()
  elif st.session_state.page == "kdrama":
        kdrama.show()
  else:
        st.write("")


    

    