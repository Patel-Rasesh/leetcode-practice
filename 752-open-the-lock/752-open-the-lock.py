class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = collections.deque([('0000', 0)])
        explored = set()
        explored.add('0000')
        turns = 1
        deadends = set(deadends)
        
        def Neighbors(position):
            neighbors = []
            
            # For each place of each digit
            for eachDigit in range(4):
                digit = position[eachDigit]
                for diff in (-1, 1):
                    
                    # -1 mod 10 = 9
                    newPosition = position[:eachDigit] + str((int(digit)+diff)%10) + position[eachDigit+1:]
                    neighbors.append(newPosition)
            return neighbors
        
        if '0000' == target:
            return 0
        
        while queue:
            currentComb, turns = queue.popleft()
            if currentComb == target:
                print(currentComb)
                return turns
            if currentComb in deadends:
                continue
            for eachComb in Neighbors(currentComb):
                if eachComb not in explored:
                    queue.append((eachComb, turns+1))
                    explored.add(eachComb)
        return -1
        # print(Neighbors('3926'))