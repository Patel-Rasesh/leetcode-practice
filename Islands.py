class Solution(object):
    def isIsland(self, grid, row, col):
        # row-1, row+1, col-1, col+1
        if row-1 < 0 or row+1 == len(grid) or col-1 < 0 or col+1 == len(grid) or grid[row][col] != '1':
            return
        else:
            grid[row][col] = '0'
        self.isIsland(grid, row-1, col)
        self.isIsland(grid, row+1, col)
        self.isIsland(grid, row, col-1)
        self.isIsland(grid, row, col+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    islands += 1
                    self.isIsland(grid, row, col)
        return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
print(obj.numIslands(grid))