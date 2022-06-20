class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # queue = collections.deque([('0000', 0)])
        queue = []
        queue.append('0000')
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
        if '0000' in deadends:
            return -1
        while queue:
            lengthOfQueue = len(queue)
            while lengthOfQueue:
                currentComb = queue.pop(0)
                for eachComb in Neighbors(currentComb):
                    if eachComb not in explored:
                        if eachComb in deadends:
                            continue
                        if eachComb == target:
                            print(eachComb)
                            return turns
                        queue.append(eachComb)
                        explored.add(eachComb)
                lengthOfQueue -= 1
            turns += 1 
        return -1
        # print(Neighbors('3926'))