import heapq

# lipo san zabija ča je ta algoritam, pa san pita Đepeta :D

def dijkstra(graph, start):
    # 1. Inicijalizacija udaljenosti
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 2. Priority queue (udaljenost, čvor)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Ako imamo bolji (kraći) put već poznat, preskoči
        if current_distance > distances[current_node]:
            continue

        # 3. Iteriraj kroz susjede
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Ako smo pronašli kraći put do susjeda
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# --- Test primjer ---
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))
# Očekivani izlaz: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
