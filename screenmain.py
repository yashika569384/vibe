import streamlit as st
import artff

st.set_page_config(page_title="VibeVerse", layout="centered")

if 'art_button_clicked' not in st.session_state:
    st.session_state.art_button_clicked=False



# Hide default Streamlit elements (optional for a clean look)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# YouTube video background HTML
video_html = """
<style>
.video-background {
  position: fixed;
  top: 0;
  left: 0;
  min-width: 100vw;
  min-height: 100vh;
  z-index: -1;
  overflow: hidden;
}
.video-background iframe {
  width: 100vw;
  height: 100vh;
  pointer-events: none;
}
</style>

<div class="video-background">
    <iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID?autoplay=1&mute=1&controls=0&loop=1&playlist=AMpnp6Nfjs6AfUAP" 
            frameborder="0" allow="autoplay; fullscreen">
    </iframe>
</div>
"""

# Replace 'YOUR_VIDEO_ID' with the actual ID from the YouTube URL
# For example, for https://www.youtube.com/watch?v=dQw4w9WgXcQ → use dQw4w9WgXcQ
video_id = "AMpnp6Nfjs6AfUAP"  # example ID
video_html = video_html.replace("Video ID", video_id)

# Inject the video background
st.markdown(video_html, unsafe_allow_html=True)

# Example foreground content

st.markdown("""
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #ffcc70;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 100px; /* Set font size to 50px */
    }
    
    
    .custom-button:hover {
        background-color: #ff9900;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }

    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #66a5ed;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 60px 80px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 100px; /* Increase font size for larger text */
        width: 300px;
        height: 200px;
    }

    div.stButton > button:first-child:hover {
        background-color: #062447;
        color: white;
        box-shadow: 0 0 15px #86a0bf, 0 0 25px #86a0bf, 0 0 35px #86a0bf;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for all buttons
for key in ["art_button_clicked", "entertainment_button_clicked", "game_button_clicked", "news_button_clicked"]:
    if key not in st.session_state:
        st.session_state[key] = False

# Main screen: show 4 buttons if no section is active
if not any([
    st.session_state.art_button_clicked,
    st.session_state.entertainment_button_clicked,
    st.session_state.game_button_clicked,
    st.session_state.news_button_clicked
]):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Art"):
            st.session_state.art_button_clicked = True
        if st.button("Game"):
            st.session_state.game_button_clicked = True

    with col2:
        if st.button("Entertainment"):
            st.session_state.entertainment_button_clicked = True
        if st.button("News"):
            st.session_state.news_button_clicked = True

# Art Section
if st.session_state.art_button_clicked:
    st.header("Art Corner")
    artff.show()  # Your art logic here

    if st.button("Back", key="back_art"):
        st.session_state.art_button_clicked = False

# Entertainment Section
elif st.session_state.entertainment_button_clicked:
    st.header("Entertainment Corner")
    st.write("Entertainment content goes here...")

    if st.button("Back", key="back_entertainment"):
        st.session_state.entertainment_button_clicked = False

# Game Section
elif st.session_state.game_button_clicked:
    st.header("Gaming Corner")
    st.write("Gaming content goes here...")

    if st.button("Back", key="back_game"):
        st.session_state.game_button_clicked = False

# News Section
elif st.session_state.news_button_clicked:
    st.header("News Room")
    st.write("News content goes here...")

    if st.button("Back", key="back_news"):
        st.session_state.news_button_clicked = False




