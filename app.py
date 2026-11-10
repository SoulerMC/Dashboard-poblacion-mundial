import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="poblacion mundial", layout="wide")

st.title("analisis de poblacion mundial")
st.write("aqui tenemos los 10 paises mas poblados del mundo")

archivo = st.file_uploader("selecciona el archivo CSV", type="csv")

if archivo is not None:
    datos = pd.read_csv(archivo)
    pais_col = "Country/Territory" if "Country/Territory" in datos.columns else "country"

    top10 = datos.sort_values("2022 population", ascending=False).head(10)

    st.dataframe(top10[[pais_col, "2015 population", "2020 population", "2022 population"]])

    paises = top10[Country/Territory].to_numpy()

    poblacion_2015 = top10["2015 population"].to_numpy()
    poblacion_2020 = top10["2020 population"].to_numpy()
    poblacion_2022 = top10["2022 population"].to_numpy()

    total = np.sum(poblacion_2022)
    promedio = np.mean(poblacion_2022)
    mediana = np.median(poblacion_2022)
    minimo = np.min(poblacion_2022)
    maximo = np.max(poblacion_2022)

    st.subheader("estadisticas de la poblacion de 2022")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("poblacion total", f"{total/1000000:,.2f} millones")
    col2.metric("promedio de poblacion", f"{promedio/1000000:,.2f} millones")
    col3.metric("mediana de poblacion", f"{mediana/1000000:,.2f} millones")
    col4.metric("poblacion minima", f"{minimo/1000000:,.2f} millones")
    col5.metric("poblacion maxima", f"{maximo/1000000:,.2f} millones")

    st.subheader("comparacion de la poblacion por paises")

    grafico = top10.set_index(pais_col)[[
        "2015 population",
        "2020 population",
        "2022 population"
    ]] / 1000000

    st.bar_chart(grafico)

    st.subheader("datos de los 10 paises")

    st.dataframe(top10[[
        "2015 population",
        "2020 population",
        "2022 population"
    ]])


