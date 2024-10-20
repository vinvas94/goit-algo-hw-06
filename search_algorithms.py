from collections import deque

# Depth-First Search (DFS)
def dfs(graph, start):
    visited, stack = set(), [start]
    paths = {start: [start]}
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    paths[neighbor] = paths[vertex] + [neighbor]
    return paths

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited, queue = set(), deque([start])
    paths = {start: [start]}
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    paths[neighbor] = paths[vertex] + [neighbor]
    return paths
