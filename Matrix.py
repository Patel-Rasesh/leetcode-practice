import numpy as np
matrix = np.array([[0, 3, 4], [3, 0, 6], [5, 6, 1]])
    
identity = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j] == 0):
            identity.append([i, j])
for pair in identity:
    matrix[pair[0]] = 0
    matrix[:, pair[1]] = 0
# After manipulation
print(matrix)