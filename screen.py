import streamlit as st


st.set_page_config(page_title='main screen')
st.markdown("""
    <style>
    .custom-button {
        background-color: #ffcc70;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;
        border-radius: 10px;
        
        padding: 0.5em 1em;
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .custom-button:hover {
        background-color: #ff9900;
        color: white;
    }
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        margin: 5px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

        