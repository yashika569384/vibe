import streamlit as st
import artff

st.set_page_config(page_title="VibeVerse", layout="centered")

if 'art_button_clicked' not in st.session_state:
    st.session_state.art_button_clicked=False


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
        width: 500px;
        height: 100px;
    }

    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
        box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)

if not st.session_state.art_button_clicked:
    if st.button("Art"):
        st.session_state.art_button_clicked = True

# if not st.session_state.enter_button_clicked:
#     if st.button("Entertainment"):
#         st.session_state.enter_button_clicked = True
  
# Show the art screen if the button was clicked
if st.session_state.art_button_clicked:
    # Replace this with your actual art screen rendering logic
    artff.show()
if st.session_state.enter_button_clicked:
    # Replace this with your actual art screen rendering logic
    # artff.show()
    st.write("")
# if "art_button_clicked" not in st.session_state:
#     st.session_state.art_button_clicked = False
# if "entertainment_button_clicked" not in st.session_state:
#     st.session_state.entertainment_button_clicked = False

# # # if page == "home":
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

