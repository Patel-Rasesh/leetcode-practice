class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1. If matrix is empty, there is no target
        if not matrix:
            return False
        def huntingTarget(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            
            # 2. If target is smaller than top-left of matrix,
            #   or target is larger than bottom-right of matrix, target is not found
            if target < matrix[top][left] or target > matrix[bottom][right]:
                return False
            
            # 3. Find the suitable quandrant for target and recursively look for Target in them
            desiredRow = top
            middle = left + (right-left)//2
            
            while desiredRow <= bottom and target >= matrix[desiredRow][middle]:
                if matrix[desiredRow][middle] == target:
                    return True
                desiredRow += 1
            
            return huntingTarget(left, middle-1, desiredRow, bottom) or huntingTarget(middle+1, right, top, desiredRow-1)
        
        return huntingTarget(0, len(matrix[0])-1, 0, len(matrix)-1)