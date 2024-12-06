# Stanisław Kusiak

def dijkstra(graph, start):
    length = len(graph)
    distances = {node: float('inf') for node in graph}
    checked = {node: False for node in graph}
    distances[start] = 0

    for _ in range(length):
        min_dist = float('inf')
        u = None
        for i in graph:
            if not checked[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u is None:
            break

        checked[u] = True

        for i in graph[u]:
            if graph[u][i] != 0 and not checked[i]:
                alt = distances[u] + graph[u][i]
                if alt < distances[i]:
                    distances[i] = alt

    return distances



graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 3},
    'D': {'B': 2, 'C': 3}
}

print(dijkstra(graph, 'A'))
