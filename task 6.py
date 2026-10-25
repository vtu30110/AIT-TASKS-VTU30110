
states = ['A', 'B', 'C', 'D']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def color_map(index):
    if index == len(states):
        return True

    state = states[index]

    for color in colors:
        if all(result.get(neighbor) != color
               for neighbor in graph[state]):
            result[state] = color

            if color_map(index + 1):
                return True

            del result[state]

    return False

if color_map(0):
    print("Map Coloring Solution:")
    for state, color in result.items():
        print(state, ":", color)
else:
    print("No solution found")
