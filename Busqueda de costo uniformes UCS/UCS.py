import heapq

def ucs(grafo, inicio, meta):
    cola = [(0, inicio)]  # (costo, nodo)
    visitados = set()
    costo_acumulado = {inicio: 0}
    padre = {inicio: None}
    
    while cola:
        costo, nodo = heapq.heappop(cola)
        
        if nodo in visitados:
            continue
            
        visitados.add(nodo)
        
        if nodo == meta:
            break
            
        for vecino, costo_arista in grafo.get(nodo, []):
            nuevo_costo = costo + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))
                padre[vecino] = nodo
    
    # Reconstruir el camino
    camino = []
    nodo_actual = meta
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = padre.get(nodo_actual)
    
    camino.reverse()
    return camino, costo_acumulado.get(meta, float('inf'))

# Grafo con costos
grafo_costo = {
    "R": [("S", 1), ("C", 1)],
    "S": [("R", 3), ("F", 1)],
    "C": [("R", 3)],
    "D": [],
    "E": [("G", 1)],
    "F": [("S", 1)],
    "G": [("E", 1)]
}

camino, costo = ucs(grafo_costo, 'R', 'F')
print('UCS - Camino:', camino, 'Costo:', costo)