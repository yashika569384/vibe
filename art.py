import streamlit as st
import cv2
import numpy as np
from PIL import Image
st.title("📸Image to Art🎨 ")
img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
# Custom CSS for buttons
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

def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
    inverted = cv2.bitwise_not(gray)  # Invert the grayscale image
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)  # Apply Gaussian Blur
    sketch = cv2.divide(gray, 255 - blurred, scale=256)  # Blend with the original gray image
    return sketch
def cartoonize_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    gray_blur = cv2.medianBlur(gray, 5)  # Apply median blur
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)  # Detect edges
    
    # Apply bilateral filter for smoothing
    color = cv2.bilateralFilter(image, d=9, sigmaColor=250, sigmaSpace=250)
    
    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cartoon_stylized = cv2.stylization(image, sigma_s=150, sigma_r=0.25)

    return cartoon_stylized



if img is not None:
    image = Image.open(img)
    image = np.array(image)  # Convert PIL image to NumPy array (for OpenCV)

    st.image(image, caption="Original Image", use_column_width=True)
    #b1=st.button("Pencil sketch")
    #b2=st.button("Cartoon")
    col1, col2 = st.columns(2)

    with col1:
     
     if st.button("✏️ Pencil Sketch"):
        sketch = pencil_sketch(image)
        # original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # st.image(sketch, caption="Pencil Sketch", use_column_width=True, channels="GRAY")
        st.image([img, sketch], caption=["Original", "Pencil Sketch"], width=300)

    with col2:
     if st.button("🎨 Cartoonize"):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cartoon_image = cartoonize_image(image)
            original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cartoon = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB)
            st.image([original, cartoon], caption=["Original", "Cartoonized"], width=300)

    # if b1:

    # # if st.button("Convert to Sketch ✏️"):
    #     sketch = pencil_sketch(image)
    #     st.image(sketch, caption="Pencil Sketch", use_column_width=True, channels="GRAY")
    # if b2:
    #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to OpenCV BGR format
    
    # # Process Image
    #     cartoon_image = cartoonize_image(image)

    #     # Convert back to RGB format for display
    #     original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     cartoon = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB)

    #     # Display results
    #     st.image([original, cartoon], caption=["Original Image", "Cartoonized Image"], width=300)
        

