import random
import numpy as np

def crear_ruta(n, inicio, fin):
    ruta = [i for i in range(n) if i not in (inicio, fin)]
    random.shuffle(ruta)
    return ruta

def poblacion_inicial(tam_poblacion, n, inicio, fin):
    return [crear_ruta(n, inicio, fin) for _ in range(tam_poblacion)]

def distancia_total(ruta, matriz, inicio, fin):
    distancia = matriz[inicio][ruta[0]]
    for i in range(len(ruta) - 1):
        distancia += matriz[ruta[i]][ruta[i + 1]]
    distancia += matriz[ruta[-1]][fin]
    return distancia

def fitness(ruta, matriz, inicio, fin):
    return 1 / distancia_total(ruta, matriz, inicio, fin)

def seleccion_torneo(poblacion, matriz, inicio, fin, k=3):
    seleccionados = random.sample(poblacion, k)
    seleccionados.sort(
        key=lambda r: fitness(r, matriz, inicio, fin),
        reverse=True
    )
    return seleccionados[0]

def cruce(padre1, padre2):
    inicio, fin = sorted(random.sample(range(len(padre1)), 2))
    hijo = [-1] * len(padre1)
    hijo[inicio:fin] = padre1[inicio:fin]

    pos = 0
    for ciudad in padre2:
        if ciudad not in hijo:
            while hijo[pos] != -1:
                pos += 1
            hijo[pos] = ciudad
    return hijo

def mutacion(ruta, tasa):
    if random.random() < tasa:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

def algoritmo_genetico(
    matriz,
    inicio,
    fin,
    generaciones=200,
    tam_poblacion=50,
    tasa_mutacion=0.1
):
    n = len(matriz)
    poblacion = poblacion_inicial(tam_poblacion, n, inicio, fin)
    mejor_ruta = None
    mejor_distancia = float("inf")
    historial = []

    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tam_poblacion):
            p1 = seleccion_torneo(poblacion, matriz, inicio, fin)
            p2 = seleccion_torneo(poblacion, matriz, inicio, fin)
            hijo = cruce(p1, p2)
            hijo = mutacion(hijo, tasa_mutacion)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion
        mejor_actual = min(
            poblacion,
            key=lambda r: distancia_total(r, matriz, inicio, fin)
        )
        dist = distancia_total(mejor_actual, matriz, inicio, fin)
        historial.append(dist)

        if dist < mejor_distancia:
            mejor_distancia = dist
            mejor_ruta = mejor_actual

    return mejor_ruta, mejor_distancia, historial


