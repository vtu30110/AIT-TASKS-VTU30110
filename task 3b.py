
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 6, 'B': 5, 'C': 4, 'D': 3,
     'E': 2, 'F': 2, 'G': 0}

def simple_astar(start, goal):
    open_list = [(h[start], 0, [start])]

    while open_list:
        open_list.sort()
        f, cost, path = open_list.pop(0)
        node = path[-1]

        if node == goal:
            print("Optimal Route:", path)
            print("Total Cost:", cost)
            return

        for next_node, weight in graph[node]:
            if next_node not in path:
                new_cost = cost + weight
                new_path = path + [next_node]
                open_list.append(
                    (new_cost + h[next_node],
                     new_cost, new_path)
                )

simple_astar('A', 'G')
