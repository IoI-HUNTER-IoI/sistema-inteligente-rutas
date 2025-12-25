import pandas as pd
import numpy as np

def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    coordenadas = df[['x', 'y']].values
    nombres = df['ciudad'].values
    return nombres, coordenadas

def matriz_distancias(coordenadas):
    n = len(coordenadas)
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matriz[i][j] = np.linalg.norm(coordenadas[i] - coordenadas[j])
    return matriz
