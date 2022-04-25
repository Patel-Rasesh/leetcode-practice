# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        def backtrack(cell = (0,0), direction = 0):
            
            # 1. Mark the current cell as visited and cleaned
            visited.add(cell)
            robot.clean()
            
            # 2. Explore four directions - forward, backward, right and left
            for index in range(4):
                localDirection = (direction + index) % 4
                localCell = (cell[0] + directions[localDirection][0],
                             cell[1] + directions[localDirection][1])    
            
                # 3. If cell is not visited and no obstacle
                if not localCell in visited and robot.move():
            
                    # 4. Move forward()
                    # 5. Recursively call 'explore' with new cell and direction
                    backtrack(localCell, localDirection)
                    
                    # 6. Backtrack to previous cell (with multidirection)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                
                # 7. Turn right (as per our fixed escape strategy) and continue
                robot.turnRight()
        
        backtrack()