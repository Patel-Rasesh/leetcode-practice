class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1
        if target > nums[high]:
            return high+1
        elif target < nums[low]:
            return 0
        derivedIndex = self.binarySearch(nums, low, high, target)
        return derivedIndex
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
obj = Solution()
#print(obj.searchInsert([1,2,12,33,47,48,49,53,57,58,61,79,93],3))
print(obj.searchInsert([1,3,5,6],7))