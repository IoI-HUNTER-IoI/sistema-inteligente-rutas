import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algoritmo_genetico import algoritmo_genetico

st.set_page_config(page_title="Sistema Inteligente de Rutas", layout="centered")

st.title("🚚 Sistema Inteligente de Optimización de Rutas")
st.write("Optimización de rutas usando Algoritmos Genéticos")

# Subida de dataset
archivo = st.file_uploader("📂 Suba el archivo CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.write("📊 Dataset cargado:")
    st.dataframe(df)

    nombres = df["ciudad"].tolist()
    coordenadas = df[["x", "y"]].values

    # Selección de inicio y fin
    inicio = st.selectbox("📍 Punto de inicio", nombres)
    fin = st.selectbox("🏁 Punto final", nombres)

    # Parámetros
    poblacion = st.slider("👥 Tamaño de población", 20, 200, 50)
    generaciones = st.slider("🔁 Generaciones", 50, 500, 200)
    mutacion = st.slider("🧬 Tasa de mutación", 0.01, 0.5, 0.1)

    if st.button("▶ Ejecutar sistema"):
        ruta, distancia, historial = algoritmo_genetico(
            coordenadas,
            nombres.index(inicio),
            nombres.index(fin),
            generaciones,
            poblacion,
            mutacion
        )

        st.success(f"✅ Distancia total: {distancia:.2f}")

        # Mostrar ruta
        ruta_nombres = [nombres[i] for i in ruta]
        st.write("➡ Ruta óptima:")
        st.write(" → ".join(ruta_nombres))

        # Gráfica
        fig, ax = plt.subplots()
        for i in range(len(ruta)):
            x, y = coordenadas[ruta[i]]
            ax.scatter(x, y)
            ax.text(x+1, y+1, f"{i}")

        x = [coordenadas[i][0] for i in ruta]
        y = [coordenadas[i][1] for i in ruta]
        ax.plot(x, y, marker="o")

        st.pyplot(fig)

        # Fitness
        st.line_chart(historial)
