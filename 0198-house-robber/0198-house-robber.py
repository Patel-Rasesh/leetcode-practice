class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # memo = [None]*n
        
        # Recursive solution with memoization
#         def robRecur(index):
#             if index >= n:
#                 return 0
#             if memo[index] is None:
#                 ignore = robRecur(index+1)
#                 best = ignore
#                 include = robRecur(index+2)+nums[index]
#                 if include > best:
#                     best = include
#                 memo[index] = best
#             return memo[index]
        
#         return robRecur(0)
        
        # DP solution
        DPTable = [None]*(n+1)
        print(DPTable)
        DPTable[n] = 0
        DPTable[n-1] = nums[n-1]
        print(DPTable)
        for index in range(n-2, -1, -1):
            DPTable[index] = max(DPTable[index+1], nums[index]+DPTable[index+2])
        print(DPTable)
        return DPTable[0]