
import random
import math
import matplotlib.pyplot as plt

# Depot and customer locations
locations = {
    0: (0, 0),
    1: (2, 3),
    2: (5, 4),
    3: (6, 1),
    4: (3, 6)
}

# Calculate distance between two points
def distance(a, b):
    x1, y1 = locations[a]
    x2, y2 = locations[b]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Calculate total route distance
def route_distance(route):
    return sum(distance(route[i], route[i+1])
               for i in range(len(route)-1))

# Generate neighboring routes by swapping customers
def get_neighbors(route):
    neighbors = []
    for i in range(1, len(route)-2):
        for j in range(i+1, len(route)-1):
            new_route = route.copy()
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    return neighbors

# Generate random route
def random_route():
    customers = [1, 2, 3, 4]
    random.shuffle(customers)
    return [0] + customers + [0]

# Hill Climbing algorithm
def hill_climbing():
    route = random_route()

    while True:
        neighbors = get_neighbors(route)
        best = min(neighbors, key=route_distance)

        if route_distance(best) >= route_distance(route):
            break

        route = best

    return route

# Find the best route
best_route = hill_climbing()

print("Best Route:", best_route)
print("Total Distance:", round(route_distance(best_route), 2))

# Draw route diagram
x = [locations[i][0] for i in best_route]
y = [locations[i][1] for i in best_route]

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-o', linewidth=2, markersize=8)

# Label depot and customers
for i, (px, py) in locations.items():
    label = "Depot" if i == 0 else f"C{i}"
    plt.text(px + 0.1, py + 0.1, label, fontsize=12)

plt.title("Vehicle Routing Problem - Hill Climbing")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.show()
