class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive solution
        n = len(nums)
        memo = [None]*n
        
        # Recursive solution
        def robRecur(index):
            if index >= n:
                return 0
            if memo[index] is None:
                ignore = robRecur(index+1)
                best = ignore
                include = robRecur(index+2)+nums[index]
                if include > best:
                    best = include
                memo[index] = best
            return memo[index]
        
        return robRecur(0)
        
        # DP solution