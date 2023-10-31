import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')

#upload_file = st.file_uploader('Upload your file here')
upload_file = '.all_day.csv'

if upload_file:
  df = pd.read_csv(upload_file)
  st.write(df.describe())

  st.header('Data Header')
  st.write(df.head())

  fig, ax = plt.subplot(1, 1)
  ax.scatter(x = df['depth'], y = df['mag'])
  ax.set_xlabel('Depth of Earthquake')
  ax.set_ylabel('Magnitude of Earthquake')

  st.pyplot(fig)

