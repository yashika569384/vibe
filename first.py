import streamlit as st
import artff
import newsai
import game
import home1
# st.set_page_config(page_title="VibeVerse", layout="centered")
if 'art_button_clicked' not in st.session_state:
    st.session_state.art_button_clicked=False
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
    """, unsafe_allow_html=True)
 
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(-45deg, #f3ec78, #af4261, #74ebd5, #acb6e5);
#         background-size: 400% 400%;
#         animation: gradientAnimation 12s ease infinite;
#         font-family: 'Courier New', Courier, monospace;
#         color: white;
#     }

#     @keyframes gradientAnimation {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#     /* Neon-style Streamlit button styling */
#     div.stButton > button:first-child {
#         background-color: #0f0f0f;
#         color:#2653d1;
#         font-weight: bold;
#         font-family: 'Courier New', Courier, monospace;
#         border: 2px solid #2653d1;
#         border-radius: 15px;
#         padding: 40px 60px;
#         font-size: 100px;
#         width: 300px;
#         height: 200px;
#         text-shadow: 0 0 5px #2653d1, 0 0 10px #2653d1;
#         box-shadow: 0 0 10px #2653d1, 0 0 20px #2653d1, 0 0 30px #2653d1;
#         transition: 0.3s ease-in-out;
#     }

#     div.stButton > button:first-child:hover {
#         background-color: #1f1f1f;
#         color: #00ffff;
#         border-color: #00ffff;
#         text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
#         box-shadow: 0 0 15px #00ffff, 0 0 25px #00ffff, 0 0 35px #00ffff;
#         transform: scale(1.05);
#     }
#     </style>
# """, unsafe_allow_html=True)
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
        background-color:#219ebc;
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
    }.py
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)

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
        if st.button("Pixel Paint"):
            st.session_state.art_button_clicked = True
        if st.button("Game Spot"):
            st.session_state.game_button_clicked = True

    with col2:
        if st.button("Fantasy World"):
            st.session_state.entertainment_button_clicked = True
        if st.button("Global Feed"):
            st.session_state.news_button_clicked = True

# Art Section
if st.session_state.art_button_clicked:
    st.header("Art Corner")
    artff.show()  # Your art logic here

    if st.button("Back", key="back_art"):
        st.session_state.art_button_clicked = False

# Entertainment Section
elif st.session_state.entertainment_button_clicked:
    # st.header("Entertainment Corner")
    # option=st.sidebar.selectbox("Select options",options=['Home','Music','Movies','K-Drama'],key='home')
    home1.show()
    if st.button("Back", key="back_enter"):
        st.session_state.entertainment_button_clicked = False

# Game Section
elif st.session_state.game_button_clicked:
    # st.header("Gaming Corner")
    
    game.show()

    if st.button("Back", key="back_game"):
        st.session_state.game_button_clicked = False

# News Section
elif st.session_state.news_button_clicked:
   
    
    newsai.show()

    if st.button("Back", key="back_news"):
        st.session_state.news_button_clicked = False




