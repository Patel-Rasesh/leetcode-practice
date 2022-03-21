class Solution(object):
    def arrayPairSum(self, nums):
        result=0
        nums.sort(reverse = True)
        runner1 = 0
        runner2 = 1  
        while runner2 < len(nums):
            result += min(nums[runner1],nums[runner2])
            runner1 += 2
            runner2 += 2
        return result
obj = Solution()
nums = [1,4,3,2]
print(obj.arrayPairSum(nums))
