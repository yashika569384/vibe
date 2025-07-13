import streamlit as st
import requests

# st.set_page_config("Live News", layout="wide")

def show():
    st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }

    .title {
        font-size: 36px;
        color: #1f77b4;
        font-weight: bold;
    }

    .news-card {
        background-color: white;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }

    .news-title {
        font-size: 24px;
        color: #333;
        font-weight: 600;
    }

    .news-desc {
        font-size: 16px;
        color: #666;
        margin-bottom: 10px;
    }

    .news-link {
        font-size: 16px;
        color: #0077cc;
        text-decoration: none;
        font-weight: bold;
    }

    .news-link:hover {
        text-decoration: underline;
    }

    </style>
""", unsafe_allow_html=True)
    st.title("📰 Live News Portal")

    # News categories
    category = st.selectbox("Select News Category:", ['Worldwide', 'Technology', 'Sports', 'Politics', 'Health', 'Crime'])

# Helper function to display articles beautifully
    def display_articles(articles):
      for article in articles:
        with st.container():
            st.markdown("---")
            col1, col2 = st.columns([4, 1.5])
            
            with col1:
                st.markdown(f"### {article.get('title', 'No Title')}")
                st.markdown(f"[🔗 Read more]({article.get('link', '#')})", unsafe_allow_html=True)
                st.write(article.get('description', ''))

            with col2:
                image_url = article.get('image_url')
                if image_url:
                    st.image(image_url, use_container_width=True)
                else:
                    st.image("https://via.placeholder.com/150", caption="No Image", use_container_width=True)

# Function to fetch and display news
    def fetch_news(api_url):
     try:
        res = requests.get(api_url)
        if res.status_code == 200:
            data = res.json()
            if 'results' in data:
                display_articles(data['results'])
            else:
                st.warning("No news results found.")
        else:
            st.error(f"Error {res.status_code}: {res.text}")
     except Exception as e:
        st.error(f"An error occurred: {e}")

# API key and URLs
    API_KEY = "pub_78420b7c31161688b349ff8afadd8823a215c"
    BASE_URL = "https://newsdata.io/api/1/news"

# Mapping category to API URL
    api_urls = {
    "Worldwide": f"{BASE_URL}?apikey={API_KEY}&country=in&language=en&category=world",
    "Technology": f"{BASE_URL}?apikey={API_KEY}&q=technology&country=in&language=en&category=technology",
    "Sports": f"{BASE_URL}?apikey={API_KEY}&q=sports&country=in&language=en&category=sports",
    "Politics": f"{BASE_URL}?apikey={API_KEY}&q=politics&country=in&language=en&category=politics",
    "Health": f"{BASE_URL}?apikey={API_KEY}&q=health&country=in&language=en&category=health",
    "Crime": f"{BASE_URL}?apikey={API_KEY}&q=crime&country=in&language=en&category=crime",
    }

# Fetch and display news
    fetch_news(api_urls[category])
