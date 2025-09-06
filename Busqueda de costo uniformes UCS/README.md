# 🧠 Algoritmo de Búsqueda de Costo Uniforme (UCS)

## 📖 Explicación del Algoritmo UCS

La Búsqueda de Costo Uniforme (UCS) es un algoritmo de búsqueda no informada que explora los nodos de un grafo según el costo acumulado más bajo, buscando la ruta más rentable desde el origen hasta el destino.


## 🔍 Cómo Funciona el Algoritmo

1. Inicialización:

    - Comienza con el nodo inicial (costo 0)

    - Utiliza una cola de prioridad (min-heap) para expandir nodos con menor costo primero

    - Mantiene registro de nodos visitados, costos acumulados y padres

2. Proceso de Búsqueda:

    - Extrae el nodo con menor costo de la cola

    - Si es el objetivo, termina la búsqueda

    - Expande los nodos vecinos y calcula nuevos costos

        Actualiza costos si encuentra un camino más barato

3. Reconstrucción del Camino:

    - Utiliza el diccionario de padres para reconstruir la ruta óptima

    - Devuelve el camino y el costo total

## 📊 Ejemplo de Ejecución

Para el grafo proporcionado:

text
R → S (costo: 1)
R → C (costo: 1)
S → R (costo: 3)
S → F (costo: 1)


El algoritmo encontrará el camino:

- Camino: R → S → F

- Costo total: 2 (1 de R a S + 1 de S a F)

## ⚙️ Componentes del Código


1. Cola de Prioridad: Utiliza heapq para gestionar eficientemente los nodos por costo

2. Estructuras de Datos:

    - visitados: Evita reprocesar nodos

    - costo_acumulado: Almacena el mejor costo conocido para cada nodo

    - padre: Permite reconstruir el camino óptimo

3. Manejo de Grafos: El grafo se representa como un diccionario de listas de tuplas (vecino, costo)

## 🎯 Aplicaciones del UCS

- Sistemas de navegación y mapas

- Planificación de rutas óptimas

- Optimización en redes

- Algoritmos de enrutamiento

## 👥 Autores
- *Carlos Andrés Suárez Torres* → [Carlos23Andres](https://github.com/Carlos23Andres)  
- *Saira Sharid Sanabria Muñoz* → [sharito202](https://github.com/sharito202)
