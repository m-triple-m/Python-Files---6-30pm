import streamlit as st
from PIL import Image, ImageFilter, ImageDraw, ImageFont


def watermark(image, text="Sample Text", font_size = 36):
    w, h = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('font.ttf', font_size)
    tw, th = draw.textsize(text, font)

    x, y = w-tw-10, h-th-10

    draw.text((x, y), text, font = font)

sidebar = st.sidebar

sidebar.title("Image Editing Webapp")
sidebar.markdown('''<hr><br>''', True)

sidebar.header("Change Size")
w = int(sidebar.number_input("Width"))
h = int(sidebar.number_input("Height"))
resizebtn = sidebar.button("Resize Image")

sidebar.header("Apply Filter")
img_filter = {
    'Detail' : ImageFilter.DETAIL,
    'Blur' : ImageFilter.BLUR,
    'Outline' : ImageFilter.CONTOUR,
    'Enhance Edges' : ImageFilter.EDGE_ENHANCE,
    'Sharpen' : ImageFilter.SHARPEN,
    'Find Edges' : ImageFilter.FIND_EDGES
}
sel_filter = sidebar.selectbox('Select the Filter to apply', list(img_filter.keys()))
add_filter = sidebar.button("Apply Filter")

st.title("Display Image")
img_file = st.file_uploader("Upload File Here")
wrapper = st.empty()

sidebar.header("Apply Watermark")
water_text = sidebar.text_input("Enter Text to Watermark")
wm_btn = sidebar.button("Apply Watermark")

if img_file:
    image = Image.open(img_file)
    wrapper.image(image, use_column_width = True)

    if w and h and resizebtn:
        image = image.resize((w, h))
        wrapper.image(image, caption= f'Resized Image to {image.size}')

    if sel_filter:
        image = image.filter(img_filter[sel_filter])
        wrapper.image(image, caption= f'Applied {sel_filter}')

    if wm_btn:
        watermark(image)
        wrapper.image(image, caption= f'Applied Watermark')
