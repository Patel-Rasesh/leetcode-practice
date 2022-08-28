class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 0a. Function to check if there is any fresh oranges
        def isThereFreshOranges(grid):
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 1:
                        return True
            return False
        def isThereRottenOranges(grid):
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 2:
                        return True
            return False
        
        # 0b. Funcation that find rotten oranges at the moment and return a list or their coordinates
        
        def findRottenOranges(grid):
            rottenOranges = []
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 2:
                        rottenOranges.append([row, col])
            return rottenOranges
        
        # 1. No fresh oranges or no rotten oranges
        if not isThereFreshOranges(grid):
            return 0
        if not isThereRottenOranges(grid):
            return -1
        
        # 2. Traverse that list and if there is a fresh orange 4-directionally to that coordinate, rotten it
        rowLength = len(grid)
        colLength = len(grid[0])
        timeLapse = 0
        flag = True
        while isThereFreshOranges(grid) and flag == True:
            timeLapse += 1
            rottenOranges = findRottenOranges(grid)
            flag = False
            for [rottenX, rottenY] in rottenOranges:
                if rottenX-1 >= 0:
                    if grid[rottenX-1][rottenY] == 1:
                        flag = True
                        grid[rottenX-1][rottenY] = 2
                if rottenX+1 < rowLength:
                    if grid[rottenX+1][rottenY] == 1:
                        flag = True
                        grid[rottenX+1][rottenY] = 2
                if rottenY-1 >= 0:
                    if grid[rottenX][rottenY-1] == 1:
                        flag = True
                        grid[rottenX][rottenY-1] = 2
                if rottenY+1 < colLength:
                    if grid[rottenX][rottenY+1] == 1:
                        flag = True
                        grid[rottenX][rottenY+1] = 2
        
        # 4. Repeat step 2 until no fresh oranges (call 0a)
        if isThereFreshOranges(grid):
            return -1
        return timeLapse