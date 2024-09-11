import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto del Sprint 6 \nLael Flores TripleTen')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construye un histograma')  # crear un botón
disp_button = st.button('Construye un grafico de dispersion')  # crear un

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Este es un histograma para el conjunto de datos de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Este es un grafico de dispersion  para el conjunto de datos de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
