import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gdp
import seaborn as sns 

a= pd.read_csv("desempleo.csv")
b= pd.read_csv("pib añocorriente.csv")
c = pd.read_csv("pib_porcentual.csv")
d = pd.read_csv("pib_real.csv")

st.title("BANCO DE LA REPUBLICA")

fig, ax = plt.subplots(2, 2, figsize=(10, 6))

ax[0,0].plot(d["Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)"].dropna())
ax[0,1].plot(d["Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  trimestral)"].dropna())
ax[1,0].plot(d["Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  año corrido)"].dropna())
ax[1,1].plot(d["Tasa de desempleo - total nacional(Dato fin de mes)"].dropna())



st.pyplot(fig)