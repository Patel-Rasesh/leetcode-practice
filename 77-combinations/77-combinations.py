class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        # 1. Call backtrack() with initial values
        def backtrack(first = 1, curr = []):
            # 2. Once length of currentList reaches k, append it to the outputList
            if len(curr) == k:
                # Deepcopying
                output.append(curr[:])
                
            # 3. Check for each integer >= first for combination with recursively
            #       Calling backtrack
            for index in range(first, n+1):
                curr.append(index)
                backtrack(index+1, curr)
            
                # 4. Pop from the list and resume from the previous step
                curr.pop()
        backtrack()
        return output
            