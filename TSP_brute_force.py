from itertools import permutations

# Graph represented as a dictionary
graph = {
    "Paris": {
        "Nantes": 34,
        "Marseille": 45,
        "Lyon": 33
    },
    "Nantes": {
        "Paris": 34,
        "Marseille": 41,
        "Lyon": 29
    },
    "Marseille": {
        "Paris": 45,
        "Nantes": 41,
        "Lyon": 15
    },
    "Lyon": {
        "Paris": 33,
        "Nantes": 29,
        "Marseille": 15
    }
}

start_city = "Paris"

# Cities to visit (excluding the starting city)
cities = list(graph.keys())
cities.remove(start_city)

best_cost = float('inf')
best_path = None

# Generate all possible routes
for route in permutations(cities):

    path = [start_city] + list(route) + [start_city]

    total_cost = 0

    for i in range(len(path) - 1):
        total_cost += graph[path[i]][path[i + 1]]

    print(path, "Cost =", total_cost)

    if total_cost < best_cost:
        best_cost = total_cost
        best_path = path

print("\nBest path:", best_path)
print("Minimum cost:", best_cost)





from itertools import permutations

graph = {
    "Paris": {
        "Nantes": 34,
        "Marseille": 33,
        "Lyon": 33
    },
    "Nantes": {
        "Marseille": 41,
        "Lyon": 29
    },
    "Marseille": {
        "Paris": 41,
        "Lyon": 15
    },
    "Lyon": {
        "Nantes": 37
    }
}

start_city = "Paris"

cities = list(graph.keys())
cities.remove(start_city)

best_cost = float("inf")
best_path = None

for route in permutations(cities):

    path = [start_city] + list(route) + [start_city]

    cost = 0
    valid = True

    for i in range(len(path) - 1):
        current = path[i]
        next_city = path[i + 1]

        # Check that the directed edge exists
        if next_city not in graph[current]:
            valid = False
            break

        cost += graph[current][next_city]

    if valid:
        print(path, "Cost =", cost)

        if cost < best_cost:
            best_cost = cost
            best_path = path

print("\nBest path:", best_path)
print("Minimum cost:", best_cost)
