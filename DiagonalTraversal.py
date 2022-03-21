import numpy as np

class Solution:
    def findDiagonalOrder(self, mat):
        output = []
        for j in range(len(mat[0])):
            tempArray = self.printInReverse(mat,0,j)
            if j % 2 == 0:
                tempArray = tempArray[::-1]
            output.extend(tempArray)
        for i in range(1,len(mat)):
            tempArray = self.printInReverse(mat,i,len(mat[0])-1)
            if (i+len(mat[0])-1) % 2 == 0:
                tempArray = tempArray[::-1]
            output.extend(tempArray)
        return output

    def printInReverse(self, mat, i, j):
        tempArray = []
        while j >= 0 and i < len(mat):
            tempArray.append(mat[i][j])
            i += 1
            j -= 1
        return tempArray

obj = Solution()
mat = []
number = 1
for row in range(3):
    tempArray = []
    for col in range(3):
        tempArray.append(number)
        number += 1
    mat.append(tempArray)
#print(mat)
print(obj.findDiagonalOrder([[2,5],[8,4],[0,-1]]))
#print(obj.printInReverse(mat,0,3))