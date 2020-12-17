import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../IMDB_data.csv")

st.title("Hello Streamlit")

st.markdown("""
                # Heading 1
                <a href="/ds">brr.</a>
""", True)

st.dataframe(df)

st.checkbox("that's it. ")
plt.plot()

# if :
#     st.write('d')