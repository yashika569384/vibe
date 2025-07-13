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
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(page_title='VibeVista')
st.title(":red[VibeVista:microphone:]")
df1 = pd.read_csv('movieorig.csv',encoding='ISO-8859-1')
df=pd.read_csv('music1.csv',encoding='ISO-8859-1')
songs=df
# df1=pd.read_csv("series_data.csv")
option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'])
if option=='Home':
 st.header("Music for You",divider='rainbow')
 left, middle, right = st.columns(3, vertical_alignment='center')
# 1st song
 s1=df.sample(n=1)
 song=s1["song_name"].iloc[0]
 poster=s1['poster'].iloc[0]
 left.image(poster,width=150)
 with left:
  st.write(song)
# 2nd song
 s2=df.sample(n=1)
 song1=s2["song_name"].iloc[0]  
 poster1=s2['poster'].iloc[0]
 middle.image(poster1,width=150)
 with middle:
  st.write(song1)
  # 3rd song
 s3=df.sample(n=1)
 song2=s3["song_name"].iloc[0]
 poster2=s3['poster'].iloc[0]
 right.image(poster2,width=150)
 with right:
  st.write(song2)
 left, middle, right = st.columns(3, vertical_alignment='center')

#  movies
 df2=pd.read_csv("movieorig.csv",encoding='ISO-8859-1')
 st.header("Movies For You",divider='green')
 left, middle, right = st.columns(3, vertical_alignment='center')
# 1st movie
 m1=df2.sample(n=1)
 mo=m1["Title"].iloc[0]
 mposter=m1['poster_path'].iloc[0]
 left.image(mposter,width=150)
 with left:
  st.write(mo)
# 2nd song
 m2=df2.sample(n=1)
 mmo=m2["Title"].iloc[0]
 mmposter=m2['poster_path'].iloc[0]
 middle.image(mmposter,width=150)
 with middle:
  st.write(mmo)
  # 3rd song
 m3=df2.sample(n=1)
 mmmo2=m3["Title"].iloc[0]
 mmmposter2=m3['poster_path'].iloc[0]
 right.image(mmmposter2,width=150)
 with right:
  st.write(mmmo2)
# kdrama
 df2=pd.read_csv("kdrama1.csv",encoding='ISO-8859-1')
 st.header("K-Drama for You",divider='blue')
 left, middle, right = st.columns(3, vertical_alignment='center')
 
# 1st movie
 k1=df2.sample(n=1)
 kd=k1["Name"].iloc[0]
 kposter=k1['Poster Path'].iloc[0]
 left.image(kposter,width=150)
 with left:
  st.write(kd)
# 2nd song
 k2=df2.sample(n=1)
 kk=k2["Name"].iloc[0]
 kkposter=k2['Poster Path'].iloc[0]
 middle.image(kkposter,width=150)
 with middle:
  st.write(kk)
  # 3rd song
 k3=df2.sample(n=1)
 kk3=k3["Name"].iloc[0]
 kkposter2=k3['Poster Path'].iloc[0]
 right.image(kkposter2,width=150)
 with right:
  st.write(kk3)
  song1=st.session_state.current_song_left
  song2=st.session_state.current_song_middle
  song3=st.session_state.current_song_right
  s_l=song1['song_name']
  s_m=song2['song_name']
  s_r=song3['song_name']

  def talk_l(so):
         engine = pyttsx3.init()
         engine.say(so)
         engine.runAndWait()
         def play_songs(so):
             if (so):
              st.write(f"Playing the song: {so}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_l + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_l}"
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
                talk_l("Please provide a song name.")
        #  play_songs(s_l)
             def play(s_l):
              url = play_songs(s_l)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
                 play(s_l)

  def talk_m(s_m):
         engine = pyttsx3.init()
         engine.say(s_m)
         engine.runAndWait()
         def play_songs(s_m):
             if (s_m):
              st.write(f"Playing the song: {s_m}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_m + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_m}"
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
             def play(s_m):
              url = play_songs(s_m)
              if url:
                st.markdown(
                   f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
             play(s_m)
if option=='Music':
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
     st.write("Song does not exist")
  else:
   st.write("")
       
  l=st.selectbox(label='Enter Language',options=['Hindi','English','Punjabi'])
  
  if l=='Hindi':
    dm=df[df['language']=='Hindi']
  
    import random
    dm=df[df['language']=='Hindi']
    if 'songs_selected' not in st.session_state:
      st.session_state.songs_selected = random.sample(dm.to_dict('records'), 9)  # Pick 2 random songs
      st.session_state.current_song_left = st.session_state.songs_selected[0]
      st.session_state.current_song_middle = st.session_state.songs_selected[1]
      st.session_state.current_song_right = st.session_state.songs_selected[2]
      st.session_state.current_song_le = st.session_state.songs_selected[3]
      st.session_state.current_song_mi = st.session_state.songs_selected[4]
      st.session_state.current_song_ri = st.session_state.songs_selected[5]
      st.session_state.current_song_lee = st.session_state.songs_selected[6]
      st.session_state.current_song_mii = st.session_state.songs_selected[7]
      st.session_state.current_song_rii = st.session_state.songs_selected[8]
# Layout columns
    left, middle, right = st.columns(3)
    song1 = st.session_state.current_song_left
    song2=st.session_state.current_song_middle
    song3=st.session_state.current_song_right
    song4= st.session_state.current_song_le 
    song5= st.session_state.current_song_mi
    song6= st.session_state.current_song_ri
    song7=st.session_state.current_song_lee
    song8=st.session_state.current_song_mii
    song9=st.session_state.current_song_rii

s_l=song1['song_name']
s_m=song2['song_name']
s_r=song3['song_name']
s_le=song4['song_name']
s_mi=song5['song_name']
s_ri=song6['song_name']
s_lee=song7['song_name']
s_mii=song8['song_name']
s_rii=song9['song_name']

def talk_r(s_r):
         engine = pyttsx3.init()
         engine.say(s_r)
         engine.runAndWait()
         def play_songs(s_r):
             if (s_r):
              st.write(f"Playing the song: {s_r}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_r + " official audio")
              url=f"https://www.youtube.com/results?search_query={s_r}"
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
         def play(s_r):
              url = play_songs(s_r)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_r)



  

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=10000, stop_words='english')
df['combined_features']=df['Genre']+df['language']
c=cv.fit_transform(df['combined_features'].values.astype('U')).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(c)
# similarity
ds  = df.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
import random
# l, m, r = st.columns(3) 
def recommand(song_name):
  index=df[df['song_name']==song_name].index[0]
  distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
  s1=[df.iloc[i[0]] for i in distance[1:7]]
#  random.shuffle(s1)
  rec = random.sample(s1, min(len(s1), 7))
  for song in rec: 
#  st.write(s1)

    songs = song['song_name']
    poster_url = song['poster']    # ✅ Access poster directly

      
    st.image(poster_url, width=150)
    st.write(songs)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
def talk_l(s_l):
        engine = pyttsx3.init()
        engine.say(s_l)
        engine.runAndWait()
        def play_songs(s_l):
            if (s_l):
             st.write(f"Playing the song: {s_l}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_l + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_l}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_l):
            url = play_songs(s_l)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_l)

def talk_m(s_m):
        engine = pyttsx3.init()
        engine.say(s_m)
        engine.runAndWait()
        def play_songs(s_m):
            if (s_m):
              st.write(f"Playing the song: {s_m}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_m + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_m}"
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
        def play(s_m):
            url = play_songs(s_m)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_m)
# recommand(s_l)      
# 1st column
s_l=song1['song_name']
s_m=song2['song_name']
s_r=song3['song_name']
s_le=song4['song_name']
s_mi=song5['song_name']
s_ri=song6['song_name']
s_lee=song7['song_name']
s_mii=song8['song_name']
s_rii=song9['song_name']
left, middle, right = st.columns(3)              
left.image(song1['poster'], width=150)
with left:
  st.write(s_l)
  if st.button("▶ Play", key="play_left"):
  # v=s_l
   talk_l(s_l)
#  if st.button("Recommend", key="rec_left"):
   st.subheader("Made For You:")
   recommand( s_l)   #recommnded songs for left
    
middle.image(song2['poster'], width=150)
with middle:
  st.write(s_m)
  if st.button("▶ Play", key="play_middle"):
  # v=s_l
    talk_m(s_m)     
    recommand(s_m)
# if st.button("Recommend", key="rec_middle")  
right.image(song3['poster'], width=150)
with right:
  st.write(s_r)
  if st.button("▶ Play", key="play_right"):
  # v=s_l
    talk_r(s_r)
  

    recommand(s_r)
  
# 2 layout columns 
import requests
def talk_le(s_le):
        engine = pyttsx3.init()
        engine.say(s_le)
        engine.runAndWait()
        def play_songs(s_le):
            if (s_le):
             st.write(f"Playing the song: {s_le}")
            query = urllib.parse.quote(s_le + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_le}"
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


def talk_mi(s_mi):
        engine = pyttsx3.init()
        engine.say(s_mi)
        engine.runAndWait()
        def play_songs(s_mi):
            if (s_mi):
             st.write(f"Playing the song: {s_mi}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mi}"
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
        def play(s_mi):
            url = play_songs(s_mi)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mi)
import urllib
def talk_ri(s_ri):
        engine = pyttsx3.init()
        engine.say(s_ri)
        engine.runAndWait()
        def play_songs(s_ri):
            if (s_ri):
             st.write(f"Playing the song: {s_ri}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_ri + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_ri}"
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
        def play(s_ri):
            url = play_songs(s_ri)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_ri)

# Left Column - Fixed Song. 2nd column
le, mi, ri = st.columns(3)
with le:
  song4= st.session_state.current_song_le
  st.image(song4['poster'], width=150)
  st.write(song4['song_name'])
  if st.button("▶ Play", key="play_le"):
      talk_le(s_le)
      recommand(s_le)
  
# Middle Column - Fixed Song 2
with mi:
  song5 = st.session_state.current_song_mi
  st.image(song5['poster'], width=150)
  st.write(song5['song_name'])
  if st.button("▶ Play", key="play_mi"):
      talk_mi(s_mi)
      recommand(s_mi)
      

# Right Column - "Now Playing" Section
with ri:
  song6 = st.session_state.current_song_ri
  st.image(song6['poster'], width=150)
  st.write(song6['song_name'])
  if st.button("▶ Play", key="play_ri"):
      talk_ri(s_ri)
      recommand(s_ri)
      
      # 3rd row
lee, mii, rii = st.columns(3)
def talk_lee(s_lee):
        engine = pyttsx3.init()
        engine.say(s_lee)
        engine.runAndWait()
        def play_songs(s_lee):
            if (s_lee):
             st.write(f"Playing the song: {s_lee}")
            
            
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_lee}"
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
def talk_mii(s_mii):
        engine = pyttsx3.init()
        engine.say(s_mii)
        engine.runAndWait()
        def play_songs(s_mii):
            if (s_mi):
             st.write(f"Playing the song: {s_mii}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mi + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_mii}"
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
        def play(s_mii):
            url = play_songs(s_mii)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_mii)
def talk_rii(s_rii):
        engine = pyttsx3.init()
        engine.say(s_rii)
        engine.runAndWait()
        def play_songs(s_rii):
            if (s_rii):
             st.write(f"Playing the song: {s_rii}")
            
            
            query = urllib.parse.quote(s_rii + " official audio")
            url=f"https://www.youtube.com/results?search_query={s_rii}"
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
        def play(s_rii):
            url = play_songs(s_rii)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_rii)
# Left Column - Fixed Song 1
with lee:
  song7= st.session_state.current_song_lee
  st.image(song7['poster'], width=150)
  st.write(song7['song_name'])
  if st.button("▶ Play", key="play_lee"):
      talk_lee(s_lee)
      recommand(s_lee)
# Middle Column - Fixed Song 2
with mii:
  song8 = st.session_state.current_song_mii
  st.image(song8['poster'], width=150)
  st.write(song8['song_name'])
  if st.button("▶ Play", key="play_mii"):
      talk_mii(s_mii)
      recommand(s_mii)

# Right Column - "Now Playing" Section
with rii:
  song9 = st.session_state.current_song_rii
  st.image(song9['poster'], width=150)
  st.write(song9['song_name'])
  if st.button("▶ Play", key="play_rii"):
      talk_rii(s_rii)
      recommand(s_rii)


#ENGLISH 
  if l=='English':
    dme=df[df['language']=='English']
  
    import random
  # dme=df[df['language']=='English']
    if 'songs_eselected' not in st.session_state:
      st.session_state.songs_eselected = random.sample(dme.to_dict('records'), 9)  # Pick 2 random songs
      st.session_state.current_song_eleft = st.session_state.songs_eselected[0]
      st.session_state.current_song_emiddle = st.session_state.songs_eselected[1]
      st.session_state.current_song_eright = st.session_state.songs_eselected[2]
      st.session_state.current_song_ele = st.session_state.songs_eselected[3]
      st.session_state.current_song_emi = st.session_state.songs_eselected[4]
      st.session_state.current_song_eri = st.session_state.songs_eselected[5]
      st.session_state.current_song_elee = st.session_state.songs_eselected[6]
      st.session_state.current_song_emii = st.session_state.songs_eselected[7]
      st.session_state.current_song_erii = st.session_state.songs_eselected[8]
# Layout columns
eleft, emiddle, eright = st.columns(3)
esong1=st.session_state.current_song_eleft
esong2=st.session_state.current_song_emiddle
esong3=st.session_state.current_song_eright
esong4= st.session_state.current_song_ele 
esong5=st.session_state.current_song_emi
esong6=st.session_state.current_song_eri
esong7=st.session_state.current_song_elee
esong8=st.session_state.current_song_emii
esong9=st.session_state.current_song_erii

es_l=esong1['song_name']
es_m=esong2['song_name']
es_r=esong3['song_name']
es_le=esong4['song_name']
es_mi=esong5['song_name']
es_ri=esong6['song_name']
es_lee=esong7['song_name']
es_mii=esong8['song_name']
es_rii=esong9['song_name']



def etalk_r(es_r):
         engine = pyttsx3.init()
         engine.say(es_r)
         engine.runAndWait()
         def play_songs(es_r):
             if (es_r):
              st.write(f"Playing the song: {es_r}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_r + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_r}"
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
                etalk_r("Please provide a song name.")
        #  play_songs(s_l)
         def eplay(es_r):
              url = play_songs(es_r)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         eplay(es_r)
  # from sklearn.feature_extraction.text import CountVectorizer
  # cv=CountVectorizer(max_features=10000, stop_words='english')
  # df['combined_features']=df['Genre']+df['language']
  # c=cv.fit_transform(df['combined_features'].values.astype('U')).toarray()
  # from sklearn.metrics.pairwise import cosine_similarity
  # similarity=cosine_similarity(c)
# similarity
  #  ds  = df.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# i#dxrandom
  #  import random
#
    # 
  # l, m, r = st.columns(3) 
def erecommand(song_name):
   index=df[df['song_name']==song_name].index[0]
   distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
   es1=[df.iloc[i[0]] for i in distance[1:7]]
  #  random.shuffle(s1)
   rec = random.sample(es1, min(len(es1), 7))
   for song in rec: 
  #  st.write(s1)
  
     songs = song['song_name']
     poster_url = song['poster']    # ✅ Access poster directly   
     st.image(poster_url, width=150)
     st.write(songs)
     
    #sl=s1.sample(n=5)
  #  st.write(s1)
def etalk_l(es_l):
         engine = pyttsx3.init()
         engine.say(es_l)
         engine.runAndWait()
         def play_songs(es_l):
             if (es_l):
              st.write(f"Playing the song: {es_l}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_l + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_l}"
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
                talk_l("Please provide a song name.")
        #  play_songs(s_l)
         def eplay(es_l):
              url = play_songs(es_l)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_l)

def etalk_m(es_m):
         engine = pyttsx3.init()
         engine.say(es_m)
         engine.runAndWait()
         def play_songs(es_m):
             if (es_m):
              st.write(f"Playing the song: {es_m}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_m + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_m}"
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
                talk_m("Please provide a song name.")
        #  play_songs(s_l)
         def eplay(es_m):
              url = play_songs(es_m)
              if url:
                st.markdown(
                   f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_m)
#  recommand(s_l)      
# 1st column
eleft, emiddle, eright = st.columns(3)              
eleft.image(esong1['poster'], width=150)
with eleft:
    st.write(es_l)
    if st.button("▶ Play", key="play_eleft"):
    # v=s_l
     etalk_l(es_l)
  #  if st.button("Recommend", key="rec_left"):
     st.subheader("Made For You:")
     erecommand(es_l)   #recommnded songs for left
     
emiddle.image(esong2['poster'], width=150)
with emiddle:
    st.write(es_m)
    if st.button("▶ Play", key="play_emiddle"):
    # v=s_l
     etalk_m(es_m)     
     erecommand(es_m)
  # if st.button("Recommend", key="rec_middle")  
eright.image(esong3['poster'], width=150)
with eright:
    st.write(es_r)
    if st.button("▶ Play", key="play_eright"):
    # v=s_l
     etalk_r(es_r)
     erecommand(es_r)
    
# 2 layout columns 
import requests
def etalk_le(es_le):
         engine = pyttsx3.init()
         engine.say(es_le)
         engine.runAndWait()
         def eplay_songse(es_le):
             if (es_le):
              st.write(f"Playing the song: {es_le}")
              query = urllib.parse.quote(es_le + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_le}"
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
                talk_le("Please provide a song name.")
        #  play_songs(s_l)
         def eplay(es_le):
              url = play_songs(es_le)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_le)


def etalk_mi(es_mi):
         engine = pyttsx3.init()
         engine.say(es_mi)
         engine.runAndWait()
         def eplay_songs(es_mi):
             if (es_mi):
              st.write(f"Playing the song: {es_mi}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_mi + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_mi}"
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
                talk_mi("Please provide a song name.")
        #  play_songs(s_l)
         def eplay(es_mi):
              url = play_songs(es_mi)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         eplay(es_mi)
import urllib
def etalk_ri(es_ri):
         engine = pyttsx3.init()
         engine.say(es_ri)
         engine.runAndWait()
         def eplay_songs(es_ri):
             if (es_ri):
              st.write(f"Playing the song: {es_ri}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_ri + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_ri}"
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
         def eplay(es_ri):
              url = play_songs(es_ri)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         eplay(es_ri)

# Left Column - Fixed Song. 2nd column
ele, emi, eri = st.columns(3)
with ele:
    esong4= st.session_state.current_song_ele
    st.image(esong4['poster'], width=150)
    st.write(esong4['song_name'])
    if st.button("▶ Play", key="play_ele"):
       etalk_le(es_le)
       erecommand(es_le)
    
# Middle Column - Fixed Song 2
with emi:
    esong5 = st.session_state.current_song_emi
    st.image(esong5['poster'], width=150)
    st.write(esong5['song_name'])
    if st.button("▶ Play", key="play_emi"):
        etalk_mi(es_mi)
        erecommand(es_mi)
        

# Right Column - "Now Playing" Section
with eri:
    esong6 = st.session_state.current_song_eri
    st.image(esong6['poster'], width=150)
    st.write(esong6['song_name'])
    if st.button("▶ Play", key="play_eri"):
        etalk_ri(es_ri)
        erecommand(es_ri)
        
        # 3rd row
elee, emii, erii = st.columns(3)
def etalk_lee(es_lee):
         engine = pyttsx3.init()
         engine.say(es_lee)
         engine.runAndWait()
         def play_songs(es_lee):
             if (es_lee):
              st.write(f"Playing the song: {es_lee}")
              
             
              query = urllib.parse.quote(es_lee + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_lee}"
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
                etalk_lee("Please provide a song name.")
        #  play_songs_l)
         def play(es_lee):
              url = play_songs(es_lee)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_lee)
def etalk_mii(es_mii):
         engine = pyttsx3.init()
         engine.say(es_mii)
         engine.runAndWait()
         def play_songs(es_mii):
             if (es_mii):
              st.write(f"Playing the song: {es_mii}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(es_mii + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_mii}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    
              if video_ids:
               return f"https://www.youtube.com/embed/{video_ids[1]}?autoplay=1"
              # else:
              #  return None
              
             else:
                st.write("Please provide a song name.")
                talk_mii("Please provide a song name.")
        #  play_songs(s_l)
         def play(es_mii):
              url = play_songs(es_mii)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_mii)
def etalk_rii(es_rii):
         engine = pyttsx3.init()
         engine.say(es_rii)
         engine.runAndWait()
         def play_songs(es_rii):
             if (es_rii):
              st.write(f"Playing the song: {es_rii}")
              
             
              query = urllib.parse.quote(es_rii + " official audio")
              url=f"https://www.youtube.com/results?search_query={es_rii}"
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
                talk_rii("Please provide a song name.")
        #  play_songs(s_l)
         def play(es_rii):
              url = play_songs(es_rii)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(es_rii)
# Left Column - Fixed Song 1
with elee:
    esong7= st.session_state.current_song_elee
    st.image(esong7['poster'], width=150)
    st.write(esong7['song_name'])
    if st.button("▶ Play", key="play_elee"):
        talk_lee(es_lee)
        recommand(es_lee)
# Middle Column - Fixed Song 2
with emii:
    esong8 = st.session_state.current_song_emii
    st.image(esong8['poster'], width=150)
    st.write(esong8['song_name'])
    if st.button("▶ Play", key="play_emii"):
        talk_mii(es_mii)
        recommand(es_mii)

# Right Column - "Now Playing" Section
with erii:
    esong9 = st.session_state.current_song_erii
    st.image(esong9['poster'], width=150)
    st.write(esong9['song_name'])
    if st.button("▶ Play", key="play_erii"):
        talk_rii(es_rii)
        recommand(es_rii)
 

  
     


     

