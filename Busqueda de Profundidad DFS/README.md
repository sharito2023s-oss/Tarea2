## 🧠 Algoritmo de Búsqueda en Profundidad (DFS)

## 📋 Descripción del Código

Este código implementa el algoritmo de Búsqueda en Profundidad (DFS - Depth-First Search) para encontrar un camino desde un nodo inicial hasta un nodo objetivo en un grafo representado como una lista de adyacencia.

## 🧩 Explicación del Algoritmo DFS

El DFS es un algoritmo de búsqueda no informada que:

- Explora un grafo o árbol profundizando lo más posible en cada rama antes de retroceder

- Utiliza una estrategia LIFO (Last In, First Out)

- Es implementado naturalmente con recursividad o una pila

- Complejidad temporal: O(V + E) donde V es el número de vértices y E el número de aristas

## 🔍 Cómo Funciona Este Código

1. Función DFS

```Python
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]  # Inicializar el camino

    if start == goal:
        return path  # Si el inicio es el objetivo, retornar el camino

    if start not in graph:
        return None  # Si el inicio no está en el grafo, retornar None

    for node in graph[start]:
        if node not in path:  # Evitar ciclos
            new_path = path + [node]  # Añadir nodo al camino
            result = dfs(graph, node, goal, new_path)  # Llamada recursiva

            if result is not None:
                return result  # Si se encuentra un camino, retornarlo

    return None  # Si no se encuentra camino, retornar None
```
2. Grafo de Ejemplo

```Python
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
    'O': [],
    'Q': [],
    'Z': [],
    'N': [],
    'G': []
}
```

3. Ejecución

```Python
start_node = 'A'
end_node = 'G'
print("DFS Path:", dfs(graph, start_node, end_node))
```

## 🧭 Proceso de Búsqueda Paso a Paso

El algoritmo explora el grafo en este orden:

```Text

    Comienza en A

    Explora el primer vecino de A: L

    Desde L, explora O (callejón sin salida)

    Retrocede y explora Q desde L (callejón sin salida)

    Retrocede a A y explora su segundo vecino: B

    Desde B, explora el primer vecino: X

    Desde X, explora Y

    Desde Y, explora J

    Desde J, explora el primer vecino: N (callejón sin salida)

    Desde J, explora el segundo vecino: M

    Desde M, encuentra G (objetivo)
```

## 📊 Resultado Esperado

```text
DFS Path: ['A', 'B', 'X', 'Y', 'J', 'M', 'G']
```
## 🎯 Características del DFS

- Ventajas:

    - Requiere poca memoria (solo almacena el camino actual)

    - Encuentra soluciones en grafos con muchos niveles

- Desventajas:

    - Puede encontrar un camino no óptimo

     -Puede quedar atrapado en ramas infinitas

    - No es completo en grafos infinitos

## 📝 Notas de Uso

Este algoritmo es ideal cuando:

- El espacio de búsqueda es grande pero la solución es profunda

- Se necesita explorar todas las posibilidades

- La optimalidad del camino no es crítica


## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  
- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)