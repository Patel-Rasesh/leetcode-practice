class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        if target > nums[high]:
            return high+1
        elif target < nums[low]:
            return 0
        return self.binarySearch(nums, low, high, target)
        
    def binarySearch(self, nums, low, high, target):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif low + 1 == high:
                return low + 1
            elif nums[mid] < target:
                return self.binarySearch(nums, mid, high, target)
            elif nums[mid] > target:
                return self.binarySearch(nums, low, mid, target)