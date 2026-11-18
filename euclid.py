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

# Example usage
coordinates = [
    (0, 1),
    (1, 2),
    (-3, 4)
]
matrix = adjacency_matrix(coordinates)
for row in matrix:
    print(row)
