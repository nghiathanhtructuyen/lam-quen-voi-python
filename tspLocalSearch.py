from itertools import permutations
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def adjacency_matrix(coordinates):
    n = len(coordinates)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

def calculate_cost(matrix, path):
    return sum(matrix[path[i]][path[i+1]] for i in range(len(path) - 1))

def tsp_local_search(matrix):
    n = len(matrix)
    path = list(range(n)) + [0]
    best_cost = calculate_cost(matrix, path)

    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if j - i == 1: continue
                new_path = path[:i] + path[i:j][::-1] + path[j:]
                new_cost = calculate_cost(matrix, new_path)
                if new_cost < best_cost:
                    path, best_cost = new_path, new_cost
                    improved = True
    return path, best_cost
    
# Example usage
coordinates = [
    (0, 1),
    (1, 2),
    (-3, 4)
]
matrix = adjacency_matrix(coordinates)
path, cost = tsp_local_search(matrix)
print("Path:", path)
print("Cost:", cost)