class Solution(object):
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        # 1. For each element in nums, check if there exists (target-element)
        # that is not equal to element
        for index, num in enumerate(nums):
            if target-num in nums and index != nums.index(target-num):
                return [index, nums.index(target-num)]