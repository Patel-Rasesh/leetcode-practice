class Solution(object):
    def dominantIndex(self, nums):
        maxDigit = max(nums)
        for element in range(len(nums)):
            if nums[element] == maxDigit:
                index = element
                continue
            elif nums[element]*2 > maxDigit:
                return -1
        return index
    
obj = Solution() 
nums = [1]
print(obj.dominantIndex(nums))