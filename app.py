import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algoritmo_genetico import algoritmo_genetico
from entrada import matriz_distancias

st.set_page_config(
    page_title="Sistema Inteligente de Rutas",
    layout="centered"
)

st.title("🚚 Sistema Inteligente de Optimización de Rutas")

st.write("Desde esta aplicación puede cargar un dataset y optimizar rutas usando Algoritmos Genéticos.")

# Subida de archivo
archivo = st.file_uploader("📂 Suba el archivo CSV de ciudades", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    st.subheader("📋 Vista previa del dataset")
    st.dataframe(df)

    coordenadas = df[['x', 'y']].values
    nombres = df['ciudad'].values

    # Parámetros configurables
    st.subheader("⚙️ Parámetros del Algoritmo Genético")

    poblacion = st.slider("Tamaño de población", 20, 200, 50)
    generaciones = st.slider("Número de generaciones", 50, 500, 200)
    tasa_mutacion = st.slider("Tasa de mutación", 0.01, 0.5, 0.1)

    # Punto inicio y fin
    st.subheader("📍 Configuración de ruta")
    inicio = st.selectbox("Punto de inicio", options=range(len(nombres)),
                           format_func=lambda x: f"{x} - {nombres[x]}")
    fin = st.selectbox("Punto final", options=range(len(nombres)),
                        format_func=lambda x: f"{x} - {nombres[x]}")

    matriz = matriz_distancias(coordenadas)

    if st.button("🚀 Calcular mejor ruta"):
        ruta, distancia, historial = algoritmo_genetico(
            matriz,
            generaciones=generaciones,
            tam_poblacion=poblacion,
            tasa_mutacion=tasa_mutacion,
            inicio=inicio,
            fin=fin
        )

        st.subheader("✅ Ruta óptima encontrada")

        ruta_completa = ruta
        ruta_texto = " → ".join([f"{i}-{nombres[i]}" for i in ruta_completa])
        st.write(ruta_texto)

        st.success(f"📏 Distancia total: {distancia:.2f}")

        # Gráfica de la ruta
        fig, ax = plt.subplots()

        x = [coordenadas[i][0] for i in ruta_completa]
        y = [coordenadas[i][1] for i in ruta_completa]

        ax.plot(x, y, marker="o")

        for i in ruta_completa:
            ax.text(
                coordenadas[i][0],
                coordenadas[i][1],
                f"{i}",
                fontsize=9,
                ha="right"
            )

        ax.set_title("Ruta Optimizada (con identificación de puntos)")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        st.pyplot(fig)

        # Evolución del fitness
        fig2, ax2 = plt.subplots()
        ax2.plot(historial)
        ax2.set_title("Evolución de la distancia")
        ax2.set_xlabel("Generaciones")
        ax2.set_ylabel("Distancia")
        st.pyplot(fig2)
