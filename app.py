import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algoritmo_genetico import algoritmo_genetico
from entrada import matriz_distancias

st.set_page_config(page_title="Sistema Inteligente de Rutas", layout="centered")

st.title("🚚 Sistema Inteligente de Optimización de Rutas")

# Cargar dataset
archivo = st.file_uploader("Sube el archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    coordenadas = df[['x', 'y']].values
    nombres = df['ciudad'].values

    matriz = matriz_distancias(coordenadas)

    if st.button("Calcular mejor ruta"):
        ruta, distancia, historial = algoritmo_genetico(matriz)

        st.subheader("📍 Ruta óptima")
        ruta_completa = ruta + [ruta[0]]

        ruta_texto = " → ".join([nombres[i] for i in ruta_completa])
        st.write(ruta_texto)
        st.success(f"Distancia total: {distancia:.2f}")

        # Gráfica de la ruta
        fig, ax = plt.subplots()
        x = [coordenadas[i][0] for i in ruta_completa]
        y = [coordenadas[i][1] for i in ruta_completa]

        ax.plot(x, y, marker="o")
        for i in ruta:
            ax.text(coordenadas[i][0], coordenadas[i][1], str(i), fontsize=9)

        ax.set_title("Ruta Optimizada")
        st.pyplot(fig)

        # Gráfica evolución
        fig2, ax2 = plt.subplots()
        ax2.plot(historial)
        ax2.set_title("Evolución de la distancia")
        ax2.set_xlabel("Generaciones")
        ax2.set_ylabel("Distancia")
        st.pyplot(fig2)
