class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first):
            # 1. Base condition
            if first == n:
                output.append(nums[:])  
            
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first+1)
                nums[i], nums[first] = nums[first], nums[i]
            
        n = len(nums)
        output = []
        backtrack(0)
        return output