matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrixTranspose = []

# for col in range(len(matrix[0])):
#     matrixTemp = []
#     for row in range(len(matrix)):
#         matrixTemp.append(matrix[row][col])
#     matrixTranspose.append(matrixTemp)        

# matrixOutput = [row[::-1] for row in matrixTranspose]
# print(matrixOutput)

# Above solution is not for in-place

for row in range(len(matrix)):
    for col in range(row, len(matrix)):
        matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

print(matrix)
for row in range(len(matrix)):
    for col in range(len(matrix)//2):
        matrix[row][col], matrix[row][len(matrix)-1-col] = matrix[row][len(matrix)-1-col], matrix[row][col]

print(matrix)