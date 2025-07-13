import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("🎨 Anime Style Transfer")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Load the TFLite model
@st.cache_resource
def load_model():
    interpreter = tf.lite.Interpreter(model_path="anime_model.tflite")
    interpreter.allocate_tensors()
    return interpreter

def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image).astype(np.float32) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def postprocess_image(image):
    image = np.squeeze(image)  # Remove batch dimension
    image = np.clip(image * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(image)

def predict(image, interpreter):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    return output

if uploaded_file is not None:
    st.image(uploaded_file, caption="Original Image", use_column_width=True)
    image = Image.open(uploaded_file).convert("RGB")

    with st.spinner("Transforming to Anime Style..."):
        interpreter = load_model()
        preprocessed = preprocess_image(image)
        output = predict(preprocessed, interpreter)
        anime_image = postprocess_image(output)

    st.image(anime_image, caption="✨ Anime Style Image", use_column_width=True)
