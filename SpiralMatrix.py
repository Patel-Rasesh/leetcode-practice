import numpy as np
class Solution:
    def isAll(self, mat):
        # return True if all the elements are -99
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != -99:
                    return False
        return True
    def spiralOrder(self, mat):
        row, col = 0, 0
        output = []
        while(self.isAll(mat) == False):
            while(col<len(mat[row]) and mat[row][col] != -99):
                output.append(mat[row][col])
                mat[row][col] = -99
                col += 1
            row += 1
            col -= 1
            while(row<len(mat) and mat[row][col] != -99):
                output.append(mat[row][col])
                mat[row][col] = -99
                row += 1
            row -= 1
            col -= 1
            while(col>=0 and mat[row][col] != -99):
                output.append(mat[row][col])
                mat[row][col] = -99
                col -= 1
            row -= 1
            col += 1
            while(row>=0 and mat[row][col] != -99):
                output.append(mat[row][col])
                mat[row][col] = -99
                row -= 1
            row += 1
        return output
        
obj = Solution()
mat = []
number = 1
for row in range(3):
    tempArray = []
    for col in range(3):
        tempArray.append(number)
        number += 1
    mat.append(tempArray)
print(mat)
print(obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

