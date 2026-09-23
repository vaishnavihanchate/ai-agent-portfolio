from collections import deque
import time


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# CASE 1: Best Case
graph1 = {
    'A': ['B'],
    'B': []
}

# CASE 2: Average Case
graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# CASE 3: Worst Case
graph3 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}


cases = [
    ("Best Case", graph1),
    ("Average Case", graph2),
    ("Worst Case", graph3)
]

for name, graph in cases:

    start_time = time.perf_counter()

    bfs(graph, 'A')

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print(name)
    print("Execution Time:", execution_time, "seconds")
    print()