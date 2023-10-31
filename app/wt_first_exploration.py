"""WT_First_Exploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W_ZECiXCd8foz_HDYPAMY6hr10BYHLKu
"""

import os
print(os.listdir())
#Check which datasets we have uploaded in our colab session

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
sns.set()

df_Zon = pd.read_csv("app/ZonAnn.Ts+dSST.csv")
st.write(df_Zon.head())

df_Zon_plot = plt.figure(figsize = (10,7))
plt.subplot(1,1)
sns.lineplot(x = "Year", y = "Glob", data = df_Zon, label = "Global")
sns.lineplot(x = "Year", y = "NHem", data = df_Zon, label = "Northern Hemisphere")
sns.lineplot(x = "Year", y = "SHem", data = df_Zon, label = "Southern Hemisphere")
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies")
plt.legend();

plt.figure(figsize = (10,7))
plt.subplot(1,1)
sns.lineplot(x = "Year", y = "Glob", data = df_Zon[df_Zon["Year"]>=1990], label = "Global")
sns.lineplot(x = "Year", y = "NHem", data = df_Zon[df_Zon["Year"]>=1990], label = "Northern Hemisphere")
sns.lineplot(x = "Year", y = "SHem", data = df_Zon[df_Zon["Year"]>=1990], label = "Southern Hemisphere")
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies")
plt.legend();

st.pyplot(df_Zon_plot)

df_co2 = pd.read_csv("app/owid-co2-data.csv")
st.write(df_co2.head())

df_co2["country"].unique()

df_co2_n = df_co2[df_co2["country"].isin(["North America", "Asia", "Europe", "World"])]

st.write(df_co2_n.head())

df_co2_plot1 = plt.figure(figsize = (10,7))
sns.relplot(x = "year", y = "share_of_temperature_change_from_ghg", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("Contribution (%)")
plt.title("Share of contribution to global warming");

st.pyplot(df_Zon_plot1)

df_co2_plot2 = plt.figure(figsize = (10,7))
sns.relplot(x = "year", y = "temperature_change_from_co2", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("Temperature change (ºC)")
plt.title("Contribution to temperature increase due to CO2");

st.pyplot(df_Zon_plot2)

df_co2_plot13 = plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes)")
plt.title("Annual total emissions of CO2");

st.pyplot(df_Zon_plot3)

df_co2_plot4 = plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2_per_capita", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes per person)")
plt.title("Annual emissions of CO2 per capita");

st.pyplot(df_Zon_plot4)

df_co2_n["gdp"] = df_co2_n['co2']/df_co2_n["co2_per_gdp"]

# Here I obtained the GDP values from the other 2 variables as "gdp" column is empty for whole continents (but "co2" and "co2_per_gdp" not)

g = sns.FacetGrid(df_co2_n, col = "country", hue = "country", height = 4)
g.map(sns.scatterplot, "gdp", "temperature_change_from_co2")
g.set_axis_labels("GDP", "Temperature change (ºC)")
g.set_titles(col_template="Temperature change vs GDP")

g.add_legend();

st.pyplot(g)

