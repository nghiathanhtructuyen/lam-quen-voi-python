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

def tsp_brute_force(matrix):
    n = len(matrix)
    min_path = None
    min_cost = float('inf')

    for perm in permutations(range(1, n)):
        current_cost = 0
        current_path = [0] + list(perm) + [0]
        for i in range(n):
            current_cost += matrix[current_path[i]][current_path[i+1]]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path

    return min_path, min_cost
    
# Example usage
coordinates = [
    (0, 1),
    (1, 2),
    (-3, 4)
]
matrix = adjacency_matrix(coordinates)
path, cost = tsp_brute_force(matrix)
print("Path:", path)
print("Cost:", cost)
