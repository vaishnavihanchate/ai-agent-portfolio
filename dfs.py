import time


def dfs(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node == target:
            return

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)


def create_graph(n):
    graph = {}

    for i in range(n - 1):
        graph[i] = [i + 1]

    graph[n - 1] = []

    return graph


n = 10000
graph = create_graph(n)

runs = 100


# BEST CASE
start = time.perf_counter()

for _ in range(runs):
    dfs(graph, 0, 0)

end = time.perf_counter()

best_time = (end - start) / runs


# AVERAGE CASE
start = time.perf_counter()

for _ in range(runs):
    dfs(graph, 0, n // 2)

end = time.perf_counter()

average_time = (end - start) / runs


# WORST CASE
start = time.perf_counter()

for _ in range(runs):
    dfs(graph, 0, n - 1)

end = time.perf_counter()

worst_time = (end - start) / runs


print("DFS Execution Time")
print("--------------------------")
print("Best Case    :", best_time, "seconds")
print("Average Case :", average_time, "seconds")
print("Worst Case   :", worst_time, "seconds")