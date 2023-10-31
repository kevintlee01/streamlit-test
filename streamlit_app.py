import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')

upload_file = st.file_uploader('Upload your file here')

if upload_file:
  df = pd.read_csv(upload_file)
  st.write(df.describe())

  st.header('Data Header')
  st.write(df.head())

  fig, ax = plt.subplot(1, 1)
  ax.scatter(x = df['Depth of Earthquake'], y = df['Magnitude of Earthquake'])
  ax.set_xlabel('Depth of Earthquake')
  ax.set_ylabel('Magnitude of Earthquake')

  st.pyplot(fig)

