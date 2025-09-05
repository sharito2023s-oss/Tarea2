Tarea 2# 🧠 Algoritmos de Búsqueda en Inteligencia Artificial

## 📖 Descripción General

Este proyecto implementa tres algoritmos fundamentales de búsqueda en inteligencia artificial: Búsqueda en Profundidad (DFS), Búsqueda en Amplitud (BFS) y Búsqueda de Costo Uniforme (UCS). Cada algoritmo resuelve el problema de encontrar caminos en grafos con diferentes estrategias y propiedades.

## 🎯 Objetivos del Proyecto

- Implementar y comprender algoritmos clásicos de búsqueda no informada

- Analizar las diferencias en comportamiento y rendimiento entre DFS, BFS y UCS

- Proporcionar ejemplos prácticos con visualizaciones claras

- Documentar aplicaciones reales de cada algoritmo

## 🧩 Implementaciones

1. Búsqueda en Profundidad (DFS)

Estrategia: Explora lo más profundo posible en cada rama antes de retroceder.

```python
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    # Implementación recursiva...
```

Características:

- Implementación recursiva natural

- Utiliza pila implícita (call stack)

- Puede encontrar soluciones no óptimas

- Bajo requerimiento de memoria


2. Búsqueda en Amplitud (BFS)

Estrategia: Explora todos los nodos nivel por nivel.

```python
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    # Implementación con cola...
```

Características:

- Encuentra siempre el camino más corto (en número de aristas)

- Requiere más memoria que DFS

- Implementado con cola (FIFO)

3. Búsqueda de Costo Uniforme (UCS)

Estrategia: Expande el nodo con menor costo acumulado.

```python
def ucs(grafo, inicio, meta):
    cola = [(0, inicio)]  # (costo, nodo)
    # Implementación con cola de prioridad...
```

Características:

- Óptimo para caminos con costos variables

- Implementado con cola de prioridad (heap)

- Versión general del algoritmo de Dijkstra

## 🔍 Análisis de Resultados

```python
graph = {
    'A': ['L', 'B'],
    'L': ['O', 'Q'],
    'B': ['X', 'C'],
    'C': ['E'],
    'E': ['Z'],
    'X': ['Y'],
    'Y': ['J'],
    'J': ['N', 'M'],
    'M': ['G'],
    # ... más nodos
}
```

## 🎯 Aplicaciones Prácticas

1. DFS Aplicado:

- Resolución de laberintos

- Análisis de árboles de decisión

- Algoritmos de backtracking

- Ordenamiento topológico

2. BFS Aplicado:

- Redes sociales (grados de separación)

- Sistemas de navegación (sin tráfico)

- Crawlers web

- Broadcast en redes

3. UCS Aplicado:

- Sistemas de GPS y navegación

- Planificación de rutas logísticas

- Optimización de redes de transporte

- Asignación de recursos

## ⚡ Consideraciones de Implementación

1. Limitaciones de DFS:

- No garantiza optimalidad

- Puede entrar en bucles infinitos

- No es completo en grafos infinitos

2. Limitaciones de BFS:

- Alto consumo de memoria en grafos con alta ramificación

- Ineficiente para soluciones profundas

3. Limitaciones de UCS:

- Requiere costos no negativos

- Mayor complejidad computacional que BFS/DFS

## 📈 Conclusiones

1. Cada algoritmo tiene ventajas específicas según el contexto:

- DFS es preferible cuando el espacio es grande y la solución es profunda

- BFS garantiza el camino más corto en grafos sin pesos

- UCS es esencial cuando los costos de las aristas varían y necesitamos la ruta más económica

La elección del algoritmo adecuado depende del problema específico, los requisitos de optimalidad y los recursos disponibles.

## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  
- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)
