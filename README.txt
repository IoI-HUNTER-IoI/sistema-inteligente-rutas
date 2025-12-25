Descripción general del funcionamiento del programa
***************************************************

El programa implementa un Sistema Inteligente de Optimización de Rutas de Transporte basado en Algoritmos Genéticos, accesible a través de una interfaz web desarrollada con Streamlit. Su objetivo principal es determinar la ruta más eficiente (de menor distancia total) para recorrer un conjunto de puntos geográficos definidos por el usuario.

Al ejecutar la aplicación desde el navegador, el usuario puede cargar un archivo CSV que contiene las coordenadas de los puntos de transporte (ciudades). Posteriormente, el sistema permite configurar los parámetros del Algoritmo Genético, tales como el tamaño de la población, el número de generaciones y la tasa de mutación, así como seleccionar un punto de inicio y un punto de fin para la ruta.

Una vez iniciada la ejecución, el sistema:
* Calcula la matriz de distancias euclidianas entre todos los puntos.
* Ejecuta el Algoritmo Genético, el cual genera, evalúa y evoluciona múltiples rutas candidatas.
* Selecciona la mejor ruta encontrada durante todo el proceso evolutivo.

Finalmente, el programa muestra:
*La ruta óptima en formato textual (orden de visita de los puntos).
*La distancia total mínima recorrida.
*Una gráfica de la ruta optimizada, donde cada punto se encuentra numerado.
*Una gráfica de la evolución del fitness, que permite visualizar la convergencia del algoritmo a lo largo de las generaciones.

De esta manera, el sistema permite analizar, visualizar y validar el proceso de optimización de rutas, demostrando de forma práctica la aplicación de técnicas de Inteligencia Artificial en problemas reales de logística y transporte.