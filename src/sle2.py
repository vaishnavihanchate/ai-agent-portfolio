
from collections import deque
import timeit

# Create a 20 x 20 grid graph
SIZE = 40

graph = {}

for row in range(SIZE):
    for col in range(SIZE):
        node = (row, col)
        neighbours = []

        if row > 0:
            neighbours.append((row - 1, col))

        if row < SIZE - 1:
            neighbours.append((row + 1, col))

        if col > 0:
            neighbours.append((row, col - 1))

        if col < SIZE - 1:
            neighbours.append((row, col + 1))

        graph[node] = neighbours


start = (0, 0)
goal = (SIZE - 1, SIZE - 1)


# Breadth First Search
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# Depth First Search
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# Run once to get paths and node counts
bfs_path, bfs_nodes = bfs(graph, start, goal)
dfs_path, dfs_nodes = dfs(graph, start, goal)


# Measure each algorithm 100 times
bfs_time = timeit.timeit(
    lambda: bfs(graph, start, goal),
    number=100
)

dfs_time = timeit.timeit(
    lambda: dfs(graph, start, goal),
    number=100
)


# Average time for one search
bfs_avg_ms = (bfs_time / 100) * 1000
dfs_avg_ms = (dfs_time / 100) * 1000


# Display results
print("----- BFS RESULTS -----")
print("Path Length:", len(bfs_path))
print("Nodes Expanded:", bfs_nodes)
print("Average Time:", bfs_avg_ms, "ms")

print("\n----- DFS RESULTS -----")
print("Path Length:", len(dfs_path))
print("Nodes Expanded:", dfs_nodes)
print("Average Time:", dfs_avg_ms, "ms")