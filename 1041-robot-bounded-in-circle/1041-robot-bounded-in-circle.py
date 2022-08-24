class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # Store coordinates of ending points after each iteration of instructions
        # If a new ending point already exists in the endPoints list, return True (circle can be formed)
        # Else return False
        (x, y) = (0,0)
        direction = 'N'
        endPoints = []
        for iterations in range(10):
            for intr in instructions:
                if intr == 'G':
                    if direction == 'N':
                        y += 1
                    elif direction == 'E':
                        x += 1
                    elif direction == 'W':
                        x -= 1
                    elif direction == 'S':
                        y -= 1
                    else:
                        # Invalid direction
                        return -1
                
                elif intr == 'L':
                    if direction == 'N':
                        direction = 'W'
                    elif direction == 'E':
                        direction = 'N'
                    elif direction == 'W':
                        direction = 'S'
                    elif direction == 'S':
                        direction = 'E'
                    else:
                        # Invalid direction
                        return -1
                    
                elif intr == 'R':
                    if direction == 'N':
                        direction = 'E'
                    elif direction == 'E':
                        direction = 'S'
                    elif direction == 'W':
                        direction = 'N'
                    elif direction == 'S':
                        direction = 'W'
                    else:
                        # Invalid direction
                        return -1
                    
                else:
                    # Invalid instruction
                    return -1
            if [x,y] in endPoints:
                return True
            endPoints.append([x, y])
            
        return False