import streamlit as st
import cv2
import numpy as np
from PIL import Image
from PIL import Image
import torch
from torchvision import transforms
from torchvision.models import vgg19
st.title("📸Virtual Art🎨")

def show():
 img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
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
 if img is not None:
    image = Image.open(img)
    image = np.array(image) 
 def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
    inverted = cv2.bitwise_not(gray)  # Invert the grayscale image
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)  # Apply GB
    sketch = cv2.divide(gray, 255 - blurred, scale=256)  # Blend with the original gray image
    return sketch
 def cartoonize_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    gray_blur = cv2.medianBlur(gray, 5)  # Apply median blur
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)  # Detect edges
    color = cv2.bilateralFilter(image, d=9, sigmaColor=250, sigmaSpace=250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cartoon_stylized = cv2.stylization(image, sigma_s=150, sigma_r=0.25)
    return cartoon_stylized
 def watercolor(image):
    watercolor = cv2.stylization(image, sigma_s=60, sigma_r=0.6)
    return watercolor
 def pastel_art_effect(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image. Check the path.")
    # Resize for consistency (optional)
    img = cv2.resize(img, (800, 800))
    # Apply bilateral filter multiple times for smooth, soft look
    pastel = img.copy()
    for i in range(3):
        pastel = cv2.bilateralFilter(pastel, d=9, sigmaColor=75, sigmaSpace=75)
    # Optional: add a light color overlay for a pastel tone
    overlay = np.full(pastel.shape, (255, 228, 225), dtype=np.uint8)  # light pink overlay
    pastel = cv2.addWeighted(pastel, 0.85, overlay, 0.15, 0)
    # Optional: reduce saturation slightly to get a chalky look
    hsv = cv2.cvtColor(pastel, cv2.COLOR_BGR2HSV)
    hsv[...,1] = hsv[...,1] * 0.6  # reduce saturation
    pastel = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    return pastel
        # Load image
 def load_image(img_path, max_size=400):
    image = Image.open(img_path).convert('RGB')
    size = min(max(image.size), max_size)
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x[:3, :, :]),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)
    return image

    # Save image
 def save_image(tensor, path):
    unloader = transforms.Compose([
        transforms.Normalize(mean=[-2.118, -2.036, -1.804],
                                std=[4.367, 4.464, 4.444]),
        transforms.ToPILImage()
    ])
    image = tensor.clone().squeeze(0)
    image = unloader(image)
    image.save(path)

    # Load content and style models
    content = load_image('your_image.jpg')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    content = content.to(device)

    # Load your fantasy watercolor model
    style_model = torch.jit.load('fantasy_watercolor_model.pth').to(device)
    with torch.no_grad():
        output = style_model(content)
    save_image(output.cpu(), 'output_watercolor_fantasy.jpg')
    if img is not None:
     image = Image.open(img)
     image = np.array(image)  # Convert PIL image to NumPy array (for OpenCV)
     st.image(image, caption="Original Image", use_container_width=True)
     col1, col2,col3,col4= st.columns(4)
     with col1:
        
        if st.button("✏️ Pencil Sketch"):
         sketch = pencil_sketch(image)
        st.image([img, sketch], caption=["Original", "Pencil Sketch"], width=300)

    with col2:
        if st.button("🎨 Cartoonize"):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cartoon_image = cartoonize_image(image)
            original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cartoon = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB)
            st.image([original, cartoon], caption=["Original", "Cartoonized"], width=300)
    with col3:
        if st.button("🖌️ Watercolor Art"):
         image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
         wc_bgr = watercolor(image_bgr)
         wc_rgb = cv2.cvtColor(wc_bgr, cv2.COLOR_BGR2RGB)
         st.image([image, wc_rgb], caption=["Original", "Watercolor Effect"], width=300)
    with col4:
        if st.button("💜Pastel Art"):
            pastel = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
            pastel = cv2.convertScaleAbs(pastel, alpha=1.1, beta=10)
            pastel = cv2.GaussianBlur(pastel, (5, 5), 0)
            noise = np.random.normal(0, 10, pastel.shape).astype(np.uint8)
            pastel = cv2.add(pastel, noise)
            pastel_bgr = cv2.cvtColor(pastel, cv2.COLOR_RGB2BGR)
            st.image([image, pastel_bgr], caption=["Original", "Pastel Effect"], width=300)
