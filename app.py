import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Población Mundial", layout="wide")

st.title("Análisis de Población Mundial")
st.write("Aquí tenemos los 10 países más poblados del mundo")

archivo = st.file_uploader("Selecciona el archivo CSV", type="csv")

if archivo is not None:
    datos = pd.read_csv(archivo)
    
    
    datos.columns = datos.columns.str.lower()

    
    pais_col = "country/territory" if "country/territory" in datos.columns else "country"
    pob_2015 = "2015 population" if "2015 population" in datos.columns else "2015 population"
    pob_2020 = "2020 population" if "2020 population" in datos.columns else "2020 population"
    pob_2022 = "2022 population" if "2022 population" in datos.columns else "2022 population"
    
   
    top10 = datos.sort_values(pob_2022, ascending=False).head(10)

    st.dataframe(top10[[pais_col, pob_2015, pob_2020, pob_2022]])

    
    paises = top10[pais_col].to_numpy()

    poblacion_2015 = top10[pob_2015].to_numpy()
    poblacion_2020 = top10[pob_2020].to_numpy()
    poblacion_2022 = top10[pob_2022].to_numpy()

    total = np.sum(poblacion_2022)
    promedio = np.mean(poblacion_2022)
    mediana = np.median(poblacion_2022)
    minimo = np.min(poblacion_2022)
    maximo = np.max(poblacion_2022)

    st.subheader("Estadísticas de la población de 2022")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Población total", f"{total/1000000:,.2f} millones")
    col2.metric("Promedio de población", f"{promedio/1000000:,.2f} millones")
    col3.metric("Mediana de población", f"{mediana/1000000:,.2f} millones")
    col4.metric("Población mínima", f"{minimo/1000000:,.2f} millones")
    col5.metric("Población máxima", f"{maximo/1000000:,.2f} millones")

    st.subheader("Comparación de la población por países")

    grafico = top10.set_index(pais_col)[[pob_2015, pob_2020, pob_2022]] / 1000000

    st.bar_chart(grafico)

    st.subheader("Datos de los 10 países")

   
    st.dataframe(top10[[pais_col, pob_2015, pob_2020, pob_2022]])



