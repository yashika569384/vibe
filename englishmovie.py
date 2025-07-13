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
df=pd.read_csv("movieorig.csv",encoding='ISO-8859-1')
df6=pd.read_csv("engmov.csv",encoding='ISO-8859-1')
mop=df6
# st.set_page_config(page_title='VibeVistanew')
# st.title(":red[VibeVista:microphone:]")

   
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
    fil_df=df6[df6.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
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
      s=fil_df['Title'].iloc[0]
      import requests
      def talk_l(s):                          
         engine = pyttsx3.init()
         engine.say(s)
         engine.runAndWait()
         def play_songs(s):
             if (s):
              st.write(f"Playing the movie: {s}")
              import urllib
              query = urllib.parse.quote(s + " official trailer")
              url=f"https://www.youtube.com/results?search_query={s}"
            #   webbrowser.open(url)
            #   print(f"Playing song: {s_l}")
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
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
         play(s)
      if st.button("▶ Play"):
         talk_l(s)
        #  play_songs(s)
        #  play(s)
    #  s1=fil_df['song_name'].iloc[1]
      st.write(s)
    #  st.write(s1)
     else: 
      lef, mid = st.columns(2)
      img1=fil_df['poster_path'].iloc[0]
      img2=fil_df['poster_path'].iloc[1]
      s1=fil_df['Title'].iloc[0]
      s2=fil_df['Title'].iloc[1]
      
      def talk_l(s1):
         engine = pyttsx3.init()
         engine.say(s1)
         engine.runAndWait()
         def play_mop(s1):
             if (s1):
              st.write(f"Playing the song: {s1}")
              
              query = urllib.parse.quote(s1 + " official trailer")
              url=f"https://www.youtube.com/results?search_query={s1}"
              response = requests.get(url)
              video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
              if video_ids:
                 return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              # else:
              #    return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
              else:
                 return None
              
             else:
                st.write("Please provide a movie name.")
                talk_l("Please provide a movie name.")
         def play(s1):
              url = play_mop(s1)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this movie 😢")
         play(s1)
      def talk_m(s2):
         engine = pyttsx3.init()
         engine.say(s2)
         engine.runAndWait()
         def play_mop(s2):
             if (s2):
              st.write(f"Playing the movie: {s2}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s2 + " official trailer")
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
              url = play_mop(s2)
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
        
      
      mid.image(img2,width=200)
      with mid:
       st.write(s2)
       if st.button("▶ Play",key="re_mid"):
        talk_m(s2)
        
    else:
     st.write("Movie does not exist")
  else:
   st.write("")
  # dom=df7[df7['original_language']=='Punjabi']
  
  # my_list = [1, 2, 3]
  # import random
  # n = 9      
  # sample=random.sample(list(df7), min(n, len(df7)))
  # st.write(sample) # sample_size = min(3, len(dom))  # Ensure sample size does not exceed population size
  # # sample = random.sample(dom, sample_size)     
  
  # import random
  # if 'mop_mselected' not in st.session_state:
  #   records = df7.to_dict('records')
  #   num_to_sample = min(9, len(records))  # Prevents sampling more than what's availables
  #   st.session_state.mop_mselected = random.sample(records, num_to_sample) 

  #   if st.session_state.mop_mselected:
  #    st.session_state.current_song_leftm = st.session_state.mop_mselected[0]
  #   else:
  #    st.warning("No song selected.")
  #   st.session_state.current_song_leftm = None  # or some default value
  import random
  if 'songs_selectede' not in st.session_state:
    st.session_state.songs_selectede = random.sample(df6.to_dict('records'), 9) # Pick 2 random songs
    st.session_state.current_song_lefte = st.session_state.songs_selectede[0]
    st.session_state.current_song_middlee = st.session_state.songs_selectede[1]
    st.session_state.current_song_righte = st.session_state.songs_selectede[2]
    st.session_state.current_song_lehe = st.session_state.songs_selectede[3]
    st.session_state.current_song_mihe = st.session_state.songs_selectede[4]
    st.session_state.current_song_rihe = st.session_state.songs_selectede[5]
    st.session_state.current_song_leehe = st.session_state.songs_selectede[6]
    st.session_state.current_song_miihe = st.session_state.songs_selectede[7]
    st.session_state.current_song_riihe = st.session_state.songs_selectede[8]

    # st.session_state.songs_mselected = random.sample(dom.to_dict('records'), 9)  # Pick 2 random songs
# Layout columns
    lefte, middlee, righte= st.columns(3)
    songe1 = st.session_state.current_song_lefte
    songe2=st.session_state.current_song_middlee
    songe3=st.session_state.current_song_righte
    songe4= st.session_state.current_song_lehe
    songe5= st.session_state.current_song_mihe
    songe6= st.session_state.current_song_rihe
    songe7=st.session_state.current_song_leehe
    songe8=st.session_state.current_song_miihe
    songe9=st.session_state.current_song_riihe

    s_le=songe1['Title']
    s_me=songe2['Title']
    s_re=songe3['Title']
    s_lee=songe4['Title']
    s_mie=songe5['Title']
    s_rie=songe6['Title']
    s_leee=songe7['Title']
    s_miie=songe8['Title']
    s_riie=songe9['Title']

  def talk_r(s_re):
         engine = pyttsx3.init()
         engine.say(s_re)
         engine.runAndWait()
         def play_mop(s_re):
             if (s_re):
              st.write(f"Playing the : {s_re}")
              
              # talk_l(f"Playing the song {(song1[''])}")
        # url = f"https://www.google.com/search?q={podcast_name}"
              query = urllib.parse.quote(s_re + " official trailer")
              url=f"https://www.youtube.com/results?search_query={s_re}"
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
                talk_r("Please provide a song name.")
        #  play_songs(s_l)
         def play(s_re):
              url = play_mop(s_re)
              if url:
                st.markdown(
                   f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
            unsafe_allow_html=True,
                 )
              else:
                 st.error("No video found for this song 😢")
         play(s_re)



  

  from sklearn.feature_extraction.text import CountVectorizer
  cv6=CountVectorizer(max_features=10000, stop_words='english')
  df6['combined_features']=df6['genres']+df6['original_language']
  c6=cv6.fit_transform(df6['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c6)
# similarity
  # ds3  = df7.drop(columns=['Genre','language','poster'])
# idx=ds[ds['song_name']==s_l].index[0]
# idxrandom
  import random
# l, m, r = st.columns(3) 
  def recommandp(movie_name):
    # index7=df7[df7['song_name']==song_name].index[0]
    idx6=df6[df6['Title']==movie_name].index[0]
    distance7 = sorted(list(enumerate(similarity[idx6])), reverse=True, key=lambda vector:vector[1])
    
    s7=[df6.iloc[i[0]] for i in distance7[1:7]]
#  random.shuffle(s1)
  
    rec = random.sample(s7, min(len(s7), 7))
    for i in rec: 
#  st.write(s1)
     movies = i['Title']
     poster_url = i['poster_path']    # ✅ Access poster directly
     st.image(poster_url, width=150)
     st.write(movies)
    
  #sl=s1.sample(n=5)
#  st.write(s1)
  import urllib
  import requests
  def talk_l(s_le):
        engine = pyttsx3.init()
        engine.say(s_le)
        engine.runAndWait()
        def play_mop(s_le):
            if (s_le):
             st.write(f"Playing the movie trailer: {s_le}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_le + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_le}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            else:
              return None
            
           
      #  play_songs(s_l)
        def play(s_le):
            url = play_mop(s_le)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_le)

  def talk_m(s_me):
        engine = pyttsx3.init()
        engine.say(s_me)
        engine.runAndWait()
        def play_mop(s_me):
            if (s_me):
              st.write(f"Playing the movie trailer: {s_me}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_me + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_me}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            
            else:
              st.write("Please provide a movie name.")
              talk_m("Please provide a movie name.")
      #  play_songs(s_l)
        def play(s_me):
            url = play_mop(s_me)
            if url:
              st.markdown(
                  f'<iframe width="300%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_me)
# recommand(s_l)      
# 1st column
  songe1 = st.session_state.current_song_lefte
  songe2=st.session_state.current_song_middlee
  songe3=st.session_state.current_song_righte
  songe4= st.session_state.current_song_lehe 
  songe5= st.session_state.current_song_mihe
  songe6= st.session_state.current_song_rihe
  songe7=st.session_state.current_song_leehe
  songe8=st.session_state.current_song_miihe
  songe9=st.session_state.current_song_riihe
  s_le=songe1['Title']                                         
  s_me=songe2['Title']  
  s_re=songe3['Title']
  s_lee=songe4['Title']
  s_mie=songe5['Title'] 
  s_rie=songe6['Title'] 
  s_leee=songe7['Title']
  s_miie=songe8['Title']
  s_riie=songe9['Title']
  lefte, middlee, righte = st.columns(3)              
  lefte.image(songe1['poster_path'], width=150)
  with lefte:
    st.write(s_le)
    if st.button("▶ Play", key="play_pleft"):
  # v=s_l
     talk_l(s_le)
#  if st.button("Recommend", key="rec_left"):
     st.subheader("Made For You:")
     recommandp(s_le)   #recommnded songs for left
    
  middlee.image(songe2['poster_path'], width=150)
  with middlee:
   st.write(s_me)
   if st.button("▶ Play", key="play_pmiddle"):
  # v=s_l
      talk_m(s_me)     
      recommandp(s_me)
# if st.button("Recommend", key="rec_middle")  
  righte.image(songe3['poster_path'], width=150)
  with righte:
    st.write(s_re)
    if st.button("▶ Play", key="play_pright"):
  # v=s_l
      talk_r(s_re)
      recommandp(s_re)
  
# 2 layout columns 
  import requests
  def talk_le(s_lee):
        engine = pyttsx3.init()
        engine.say(s_lee)
        engine.runAndWait()
        def play_mop(s_lee):
            if (s_lee):
             st.write(f"Playing the movie: {s_lee}")
            query = urllib.parse.quote(s_lee + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_lee}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a movie name.")
              talk_le("Please provide a movie name.")
      #  play_songs(s_l)
        def play(s_lee):
            url = play_mop(s_lee)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_lee)


  def talk_mi(s_mie):
        engine = pyttsx3.init()
        engine.say(s_mie)
        engine.runAndWait()
        def play_mop(s_mie):
            if (s_mie):
             st.write(f"Playing the movie: {s_mie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_mie + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_mie}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a movie name.")
              talk_mi("Please provide a movie name.")
      #  play_songs(s_l)
        def play(s_mie):
            url = play_mop(s_mie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_mie)
  import urllib
  def talk_ri(s_rie):
        engine = pyttsx3.init()
        engine.say(s_rie)
        engine.runAndWait()
        def play_mop(s_rihe):
            if (s_rihe):
             st.write(f"Playing the movie: {s_rie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_rie + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_rie}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a movie name.")
              talk_r("Please provide a movue name.")
      #  play_songs(s_l)
        def play(s_rie):
            url = play_mop(s_rie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this movie 😢")
        play(s_rie)

# Left Column - Fixed Song. 2nd column

  lehe, mihe, rihe = st.columns(3)
  with lehe:
    songe4= st.session_state.current_song_lehe
    st.image(songe4['poster_path'], width=150)
    st.write(songe4['Title'])
    if st.button("▶ Play", key="play_ple"):
      talk_le(s_lee)
      recommandp(s_leee)
# Middle Column - Fixed Song 2
  with mihe:
    songe5 = st.session_state.current_song_mihe
    st.image(songe5['poster_path'], width=150)
    st.write(songe5['Title'])
    if st.button("▶ Play", key="play_pmi"):
      talk_mi(s_mie)
      recommandp(s_mie)
      

# Right Column - "Now Playing" Section
  with rihe:
    songe6 = st.session_state.current_song_rihe
    st.image(songe6['poster_path'], width=150)
    st.write(songe6['Title'])
    if st.button("▶ Play", key="play_pri"):
      talk_ri(s_rie)
      recommandp(s_rie)
      
      # 3rd row
  leepe, miipe, riipe = st.columns(3)
  def talk_lee(s_leee):
        engine = pyttsx3.init()
        engine.say(s_leee)
        engine.runAndWait()
        def play_mop(s_leee):
            if (s_leee):
             st.write(f"Playing the song: {s_leee}")
            query = urllib.parse.quote(s_leee + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_leee}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_lee("Please provide a song name.")
      #  play_songs_l)
        def play(s_leee):
            url = play_mop(s_leee)
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
        def play_mop(s_miie):
            if (s_miie):
             st.write(f"Playing the song: {s_miie}")
            
            # talk_l(f"Playing the song {(song1[''])}")
      # url = f"https://www.google.com/search?q={podcast_name}"
            query = urllib.parse.quote(s_miie + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_miie}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_mii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_miie):
            url = play_mop(s_miie)
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
        def play_mop(s_riie):
            if (s_riie):
             st.write(f"Playing the song: {s_riie}")
            
            
            query = urllib.parse.quote(s_riie + " official trailer")
            url=f"https://www.youtube.com/results?search_query={s_riie}"
          #   webbrowser.open(url)
          #   print(f"Playing song: {s_l}")
            response = requests.get(url)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
  
            if video_ids:
              return f"https://www.youtube.com/embed/{video_ids[0]}?autoplay=1"
            # else:
            #   return None
            
            else:
              st.write("Please provide a song name.")
              talk_rii("Please provide a song name.")
      #  play_songs(s_l)
        def play(s_riie):
            url = play_mop(s_riie)
            if url:
              st.markdown(
                  f'<iframe width="400%" height="700px" src="{url}" frameborder="0" allow="autoplay" allowfullscreen></iframe>',
          unsafe_allow_html=True,
                )
            else:
                st.error("No video found for this song 😢")
        play(s_riie)
# Left Column - Fixed Song 1
  with leepe:
    songe7= st.session_state.current_song_leehe
    st.image(songe7['poster_path'], width=150)
    st.write(songe7['Title'])
    if st.button("▶ Play", key="play_plee"):
      talk_lee(s_leee)
      recommandp(s_leee)
# Middle Column - Fixed Song 2
  with miipe:
    songe8 = st.session_state.current_song_miihe
    st.image(songe8['poster_path'], width=150)
    st.write(songe8['Title'])
    if st.button("▶ Play", key="play_pmii"):
      talk_mii(s_miie)
      recommandp(s_miie)

# Right Column - "Now Playing" Section
  with riipe:
    songe9 = st.session_state.current_song_riihe
    st.image(songe9['poster_path'], width=150)
    st.write(songe9['Title'])
    if st.button("▶ Play", key="play_prii"):
      talk_rii(s_riie)
      recommandp(s_riie)

# show()