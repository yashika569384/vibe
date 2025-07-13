page = st.session_state.get("page", "home")

def go_to_page(pg):
    st.session_state.page = pg
Inject CSS + HTML
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 80px;
    }

    h1 {
        font-size: 3rem;
        margin-bottom: 40px;
        text-align: center;
        text-shadow: 0 0 10px #fff;
    }

    .button-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        justify-content: center;
        max-width: 800px;
    }

    .glow-btn {
        padding: 25px 60px;
        font-size: 22px;
        font-weight: 700;
        border: 2px solid white;
        border-radius: 16px;
        background-color: transparent;
        color: white;
        
        cursor: pointer;
        transition: 0.4s ease;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 10px rgba(255,255,255,0.1);
        width: 45%;  /* Two buttons per row */
        min-width: 250px;
        text-align: center;
    }

    .soft-glow:hover {
        box-shadow: 0 0 20px #ffffff, 0 0 40px #ffffff;
    }

    .neon-glow {
        border-color: #0ff;
        color: #0ff;
    }
    .neon-glow:hover {
        box-shadow: 0 0 10px #0ff, 0 0 25px #0ff, 0 0 40px #0ff;
    }

    .border-glow {
        border-color: #ff00ff;
        color: #ff00ff;
    }
    .border-glow:hover {
        box-shadow: inset 0 0 15px #ff00ff, 0 0 30px #ff00ff;
    }

    .rainbow-glow {
        background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet);
        background-size: 400% 400%;
        animation: rainbow 5s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-color: #fff;
    }
    .rainbow-glow:hover {
        box-shadow: 0 0 10px red, 0 0 20px orange, 0 0 30px yellow, 0 0 40px green;
    }

    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>

    <div class="container">
        <h1>✨ VibeVerse</h1>
        <div class="button-container">
            <button class="glow-btn soft-glow" onclick="showScreen('artff')">Art</button>
            <button class="glow-btn neon-glow">Games</button>
            <button class="glow-btn border-glow">Entertainment</button>
            <button class="glow-btn rainbow-glow">News</button>
        </div>
    </div>
            

    
            
 """, unsafe_allow_html=True)
