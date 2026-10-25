
from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Breadth First Search (BFS) using recursion
def bfs(graph, start, target):
    queue = deque([start])
    visited = {start}

    def search():
        if not queue:
            return False

        node = queue.popleft()
        print(node, end=" ")

        if node == target:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        return search()

    search()

# Depth First Search (DFS) using recursion
def dfs(graph, node, target, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return False

    visited.add(node)
    print(node, end=" ")

    if node == target:
        return True

    for neighbor in graph[node]:
        if dfs(graph, neighbor, target, visited):
            return True

    return False

# Main program
start = input("Enter starting node (A-F): ").upper()
target = input("Enter target node (A-F): ").upper()

if start not in graph or target not in graph:
    print("Invalid node!")
else:
    print("\nBFS Traversal:")
    bfs(graph, start, target)

    print("\n\nDFS Traversal:")
    dfs(graph, start, target)

    print()
