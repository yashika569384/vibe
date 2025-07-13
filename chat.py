import streamlit as st

# Inject custom HTML and CSS
st.markdown("""
    <style>
    .button-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin-top: 50px;
    }

    .custom-btn {
        padding: 15px 25px;
        font-size: 16px;
        border: none;
        color: white;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .btn-1 {
        background-color: #ff4d4d;
    }
    .btn-1:hover {
        box-shadow: 0 0 20px #ff4d4d, 0 0 30px #ff4d4d;
    }

    .btn-2 {
        background-color: #4CAF50;
    }
    .btn-2:hover {
        transform: translateY(-5px);
    }

    .btn-3 {
        background-color: #2196F3;
    }
    .btn-3:hover {
        animation: bounce 0.4s;
    }

    @keyframes bounce {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }

    .btn-4 {
        background-color: #9C27B0;
    }
    .btn-4:hover {
        transform: rotate(360deg);
    }
    </style>

    <div class="button-container">
        <button class="custom-btn btn-1">Glow</button>
        <button class="custom-btn btn-2">Slide</button>
        <button class="custom-btn btn-3">Bounce</button>
        <button class="custom-btn btn-4">Spin</button>
    </div>
""", unsafe_allow_html=True)

st.write("⬆️ These are HTML + CSS animated buttons.")
