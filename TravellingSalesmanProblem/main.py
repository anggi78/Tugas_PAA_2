import math

def tsp(cities):
    n = len(cities)
    path = list(range(n))
    best_distance = float('inf')
    best_path = path.copy()

    def distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def calculate_distance(path):
        dist = 0
        for i in range(n-1):
            dist += distance(cities[path[i]], cities[path[i+1]])
        dist += distance(cities[path[-1]], cities[path[0]])
        return dist

    def permute(path, i):
        nonlocal best_distance, best_path
        if i == n:
            d = calculate_distance(path)
            if d < best_distance:
                best_distance = d
                best_path = path.copy()
        else:
            for j in range(i, n):
                path[i], path[j] = path[j], path[i]
                permute(path, i+1)
                path[i], path[j] = path[j], path[i]

    permute(path, 1)

    return best_path, best_distance

cities = [(0,0), (1,1), (2,2), (3,3), (4,4)]
best_path, best_distance = tsp(cities)
print("Best path is:", best_path)
print("Best distance is:", best_distance)
