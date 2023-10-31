import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')

#upload_file = st.file_uploader('Upload your file here')
upload_file = 'app/all_day.csv'

if upload_file:
  df = pd.read_csv(upload_file)
  st.write(df.describe())

  st.header('Data Header')
  st.write(df.head())

  fig, ax = plt.subplots(1, 1)
  ax.scatter(x = df['depth'], y = df['mag'])
  ax.set_xlabel('Depth of Earthquake')
  ax.set_ylabel('Magnitude of Earthquake')

  st.pyplot(fig)

components.iframe('https://docs.google.com/presentation/d/1Vh8ZytpGxqdy3oJA0bb1I-xUNjT4az5DfEve7O8myWY/edit?usp=sharing')


