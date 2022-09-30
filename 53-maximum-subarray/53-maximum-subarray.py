import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Start from the left most index.
        global_max = max(nums)
        local_sum = 0
        
        
        for i in range(len(nums)):
            
            # 1a. If that is negative, skip to the next index.
            local_sum += nums[i]
            if local_sum < 0:
                local_sum = 0
                continue
                
            # 1b. Else, keep adding subsequent element to it.
            # 2. Maintain the max when you skip an element and start over.
            global_max = max(global_max, local_sum)
            
            
        return global_max
        
        
        