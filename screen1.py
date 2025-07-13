import streamlit as st
import artff
# import newsai
# import game
# import home
st.set_page_config(page_title="VibeVerse", layout="centered")
# if 'screen' not in st.session_state:
st.title("Welcome!")
#     st.session_state.screen = 'art'
# def go_to_art_screen():
#     st.session_state.screen = 'art'

# page = st.session_state.get("page", "home")

# def go_to_page(pg):
#     st.session_state.page = pg
# Inject CSS + HTML
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

#     html, body, [class*="css"]  {
#         font-family: 'Poppins', sans-serif;
#         background: linear-gradient(to right, #141e30, #243b55);
#         color: white;
#     }

#     .container {
#         display: flex;
#         flex-direction: column;
#         align-items: center;
#         margin-top: 80px;
#     }

#     h1 {
#         font-size: 3rem;
#         margin-bottom: 40px;
#         text-align: center;
#         text-shadow: 0 0 10px #fff;
#     }

#     .button-container {
#         display: flex;
#         flex-wrap: wrap;
#         gap: 30px;
#         justify-content: center;
#         max-width: 800px;
#     }

#     .glow-btn {
#         padding: 25px 60px;
#         font-size: 22px;
#         font-weight: 700;
#         border: 2px solid white;
#         border-radius: 16px;
#         background-color: transparent;
#         color: white;
        
#         cursor: pointer;
#         transition: 0.4s ease;
#         backdrop-filter: blur(10px);
#         box-shadow: 0 0 10px rgba(255,255,255,0.1);
#         width: 45%;  /* Two buttons per row */
#         min-width: 250px;
#         text-align: center;
#     }

#     .soft-glow:hover {
#         box-shadow: 0 0 20px #ffffff, 0 0 40px #ffffff;
#     }

#     .neon-glow {
#         border-color: #0ff;
#         color: #0ff;
#     }
#     .neon-glow:hover {
#         box-shadow: 0 0 10px #0ff, 0 0 25px #0ff, 0 0 40px #0ff;
#     }

#     .border-glow {
#         border-color: #ff00ff;
#         color: #ff00ff;
#     }
#     .border-glow:hover {
#         box-shadow: inset 0 0 15px #ff00ff, 0 0 30px #ff00ff;
#     }

#     .rainbow-glow {
#         background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet);
#         background-size: 400% 400%;
#         animation: rainbow 5s ease infinite;
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         border-color: #fff;
#     }
#     .rainbow-glow:hover {
#         box-shadow: 0 0 10px red, 0 0 20px orange, 0 0 30px yellow, 0 0 40px green;
#     }

#     @keyframes rainbow {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }
#     </style>

#     <div class="container">
#         <h1>✨ VibeVerse</h1>
#         <div class="button-container">
#             <button class="glow-btn soft-glow" onclick="showScreen('artff')">Art</button>
#             <button class="glow-btn neon-glow">Games</button>
#             <button class="glow-btn border-glow">Entertainment</button>
#             <button class="glow-btn rainbow-glow">News</button>
#         </div>
#     </div>
            

    
            
#  """, unsafe_allow_html=True)


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
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 60px 80px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 50px; /* Increase font size for larger text */
        width: 300px;
        height: 100px;
    }
                                                   
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
        box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:50px;
            }
    </style>
""", unsafe_allow_html=True)
l,r=st.columns(2)
with l:
 if st.button("Art"):
  # artff.show()
  
    artff.show()
 else:
  st.write("")
#  elif st.button("News"):
# #    newsai.show()
#   st.write("")
# with r:
#  if st.button("Games"):
# #    game.show()
#   st.write("")
#  elif st.button("Entertainment"):
# #    home.show()
#   st.write("")
# # Show the art screen if the button was clicked

    # Replace this with your actual art screen rendering logartff.show()
# # if page == "home":
# #     st.markdown("""
# #         <div class="container">
# #             <h1>✨ VibeVerse</h1>
# #             <div class="button-container">
# #     """, unsafe_allow_html=True)

# #     col1, col2 = st.columns(2)

# #     with col1:
# #         if st.button("🎨 Art", key="art"):
# #             go_to_page("artff")
# # if st.button("Art"):
# #    artff.show()

