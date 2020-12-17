import streamlit as st
import pandas as pd

df = pd.read_csv('Employee_data.csv')

st.title("My Streamlit App")

st.text("So easy to create webapp")

st.checkbox("On")
st.checkbox("OFF")

data = [{'name' : 'Shawshank Redemption', 'rating' : 9.2}, {'name' : 'Batman dark knight', 'rating' : 8.7}]


st.code(data)
st.write(data)

st.info('hey')


sidebar = st.sidebar

sidebar.title("Sidebar Title Text")
box_value = sidebar.text_input("Value")
btn = sidebar.button("Submit")

if(btn):

    sidebar.info('Button Clicked')
    sidebar.error('Button Clicked')
    sidebar.warning('Button Clicked')
    sidebar.success('Button Clicked')

sli_value = sidebar.slider("myslider", max_value = 500, value=200)

st.write(f"Slider Value {sli_value}")

st.dataframe(df[0:sli_value])

st.markdown(""""

# Hello Markdown
- item1
- item2

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png">

""", True)