# 🧠 Algoritmo de Búsqueda en Amplitud (BFS) - Explicación

## 📋 Descripción del Código

Este código implementa el algoritmo de Búsqueda en Amplitud (BFS - Breadth-First Search) para encontrar el camino más corto entre dos nodos en un grafo representado como una lista de adyacencia.



## 🧩 Componentes del Código

1. Estructuras de Datos

- visited: Conjunto para mantener registro de nodos ya visitados

- queue: Cola (implementada con deque) que almacena los caminos a explorar

2. Función BFS

```Python
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    # ... implementación del algoritmo
```

3. Grafo de Ejemplo

```Python
graph = {
    'A': ['L', 'B'],
    'L': ['O', 'Q'],
    'B': ['X', 'C'],
    # ... más nodos y conexiones
}
```

## 🔍 ¿Cómo Funciona el BFS?


#### Concepto Fundamental

El BFS explora todos los nodos nivel por nivel, comenzando desde el nodo inicial y expandiéndose gradualmente hacia afuera.
Pasos del Algoritmo

1. Inicialización:

    - Se marca el nodo inicial como el primer camino a explorar

    - Se inicializa la cola con el camino que contiene solo el nodo inicial

2. Procesamiento:

    - Mientras haya caminos en la cola:

        - Se extrae el primer camino de la cola

        - Se obtiene el último nodo de ese camino

        - Si el nodo no ha sido visitado:

            - Se obtienen todos sus vecinos

            - Para cada vecino, se crea un nuevo camino (camino actual + vecino)

            - Si el vecino es el objetivo, se retorna el camino

            - Si no, se añade el nuevo camino al final de la cola

        - Se marca el nodo como visitado

3. Terminación:

    - Si se encuentra el objetivo, se retorna el camino

    - Si la cola se vacía sin encontrar el objetivo, se retorna un mensaje de error

## 🎯 ¿Qué se Buscó en Este Ejemplo?


- Nodo inicial: 'A'

- Nodo objetivo: 'G'

- Objetivo: Encontrar el camino más corto desde 'A' hasta 'G'

Ejecución Paso a Paso (Simplificada)

```text
    Comienza con: [['A']]

    Expande 'A': genera caminos [A→L] y [A→B]

    Expande 'L': genera caminos [A→L→O] y [A→L→Q] (ambos sin solución)

    Expande 'B': genera caminos [A→B→X] y [A→B→C]

    Expande 'X': genera camino [A→B→X→Y]

    Expande 'C': genera camino [A→B→C→E]

    Expande 'Y': genera camino [A→B→X→Y→J]

    Expande 'E': genera camino [A→B→C→E→Z] (sin solución)

    Expande 'J': genera caminos [A→B→X→Y→J→N] y [A→B→X→Y→J→M]

    Expande 'M': genera camino [A→B→X→Y→J→M→G] → ¡OBJETIVO ENCONTRADO!
```

## 📊 Resultado Esperado

El algoritmo retornará el camino:

```text
['A', 'B', 'X', 'Y', 'J', 'M', 'G']
```
Este es el camino más corto desde 'A' hasta 'G' en el grafo proporcionado.

## ⚡ Características del BFS

- Completitud: Siempre encuentra una solución si existe

- Optimalidad: Encuentra el camino más corto (menor número de aristas)

- Complejidad temporal: O(V + E) donde V es el número de vértices y E el número de aristas

- Complejidad espacial: O(V) en el peor caso

## 🧠 Aplicaciones del BFS

- Encontrar el camino más corto en grafos no ponderados

- Recorrido nivel por nivel en árboles

- Resolución de puzzles y problemas de búsqueda

- Análisis de redes sociales (encontrar conexiones)

- Sistemas de navegación y GPS



## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  
- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)