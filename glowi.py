import streamlit as st

st.set_page_config(page_title="Glowing Buttons Demo", layout="centered")

# Inject HTML & CSS
st.markdown("""
    <style>
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 50px;
    }

    .glow-btn {
        padding: 15px 40px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background-color: transparent;
        border: 2px solid white;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s ease-in-out;
        text-shadow: 0 0 5px #fff;
    }

    /* Soft Glow */
    .soft-glow:hover {
        box-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
    }

    /* Neon Glow */
    .neon-glow {
        border: 2px solid #0ff;
        color: #0ff;
    }
    .neon-glow:hover {
        box-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;
    }

    /* Border Glow */
    .border-glow {
        border: 2px solid #ff00ff;
        color: #ff00ff;
    }
    .border-glow:hover {
        box-shadow: inset 0 0 10px #ff00ff, 0 0 20px #ff00ff;
    }

    /* Rainbow Glow */
    .rainbow-glow {
        border: 2px solid #fff;
        color: #fff;
        background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet);
        background-size: 400% 400%;
        animation: rainbow 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .rainbow-glow:hover {
        box-shadow: 0 0 10px red, 0 0 15px orange, 0 0 20px yellow, 0 0 25px green;
    }

    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    </style>

    <div class="button-container">
        <button class="glow-btn soft-glow">Soft Glow</button>
        <button class="glow-btn neon-glow">Neon Glow</button>
        <button class="glow-btn border-glow">Border Glow</button>
        <button class="glow-btn rainbow-glow">Rainbow Glow</button>
    </div>
""", unsafe_allow_html=True)

st.write("✨ Four types of glow buttons with CSS animation! Want click functionality too?")
