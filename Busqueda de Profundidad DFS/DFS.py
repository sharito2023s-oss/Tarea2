def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]  # Initialize the path

    if start == goal:
        return path  # If start is goal, return the path

    if start not in graph:
        return None  # If start is not in graph, return None

    for node in graph[start]:
        if node not in path:  # Avoid cycles
            new_path = path + [node]  # Append node to the path
            result = dfs(graph, node, goal, new_path)  # Recursive call

            if result is not None:
                return result  # If a path is found, return it

    return None  # If no path is found, return None

# Graph represented as an adjacency list
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

start_node = 'A'
end_node = 'G'
print("DFS Path:", dfs(graph, start_node, end_node))