
import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('J', 4)],
    'E': [('J', 2)],
    'F': [('J', 5)],
    'J': []
}

# Heuristic values
h = {'A': 7, 'B': 6, 'C': 5, 'D': 4,
     'E': 2, 'F': 4, 'J': 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", cost)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(
                    queue,
                    (new_cost + h[neighbor], new_cost,
                     neighbor, path + [neighbor])
                )

astar('A', 'J')
