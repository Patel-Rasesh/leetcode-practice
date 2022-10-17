class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        DPTable = [None] * (n+1)
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        DPTable[0] = 0
        DPTable[1] = 1
        DPTable[2] = 1
        
        for i in range(3, n+1):
            DPTable[i] = DPTable[i-1] + DPTable[i-2] + DPTable[i-3]
        
        return DPTable[n]