import streamlit as st
from PIL import Image, ImageFilter

bar = st.sidebar

bar.title("Image Editor")
bar.header("Control Panel")
bar.subheader("Resize Image")

image = st.file_uploader("Upload Image Here")

if image:
    print(image)
    p_image = Image.open(image)
