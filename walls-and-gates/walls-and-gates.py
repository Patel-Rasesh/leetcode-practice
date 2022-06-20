class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Locate gates
        gates = []
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == 0:
                    gates.append([row, col])
        
        def FindNeighbors(source):
            '''
            Gives adjacent cells
            '''
            row, col = source
            neighbors = []
            if row-1 >= 0:
                neighbors.append([row-1, col])
            if row+1 < len(rooms):
                neighbors.append([row+1, col])
            if col-1 >= 0:
                neighbors.append([row, col-1])
            if col+1 < len(rooms[row]):
                neighbors.append([row, col+1])

            return neighbors
        
        def BFS(source):
            '''
            Accepts gate's coordinates as a starting point and runs BFS to each cell
            '''
            queue = [source]
            visited = []
            visited.append(source)
            BFSlevel = 1

            while queue:
                length = len(queue)
                while length:
                    currentCell = queue.pop(0)
                    neighbors = FindNeighbors(currentCell)
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            tempRow, tempCol = neighbor
                            if rooms[tempRow][tempCol] != -1 and rooms[tempRow][tempCol] != 0:
                                tempValue = min(rooms[tempRow][tempCol], BFSlevel)
                                rooms[tempRow][tempCol] = tempValue
                                queue.append(neighbor)
                                visited.append(neighbor)
                    length -= 1
                BFSlevel += 1
        # For each gate run BFS
        for eachGate in gates:
            BFS(eachGate)