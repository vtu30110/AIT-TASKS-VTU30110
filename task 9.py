
import random

random.seed(1)

dist = [
    [0, 2, 4, 5],
    [2, 0, 3, 4],
    [4, 3, 0, 2],
    [5, 4, 2, 0]
]

n = len(dist)
pheromone = [[1.0] * n for _ in range(n)]
best_route = None
best_distance = float('inf')

for iteration in range(50):
    for ant in range(10):
        route = [0]
        remaining = list(range(1, n))

        while remaining:
            current = route[-1]
            next_city = min(
                remaining,
                key=lambda city:
                dist[current][city] /
                pheromone[current][city]
            )
            route.append(next_city)
            remaining.remove(next_city)

        route.append(0)
        length = sum(dist[route[i]][route[i+1]]
                     for i in range(n))

        if length < best_distance:
            best_distance = length
            best_route = route[:]

    # Update pheromone values
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= 0.8

    for i in range(n):
        a, b = best_route[i], best_route[i+1]
        pheromone[a][b] += 1 / best_distance
        pheromone[b][a] += 1 / best_distance

print("Best Route:", best_route)
print("Minimum Distance:", best_distance)
