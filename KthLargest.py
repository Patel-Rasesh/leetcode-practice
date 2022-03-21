class Solution(object):
    def findKthLargest(self, nums, k):

        return list(sorted(nums, reverse=True))[k-1]
obj = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(obj.findKthLargest(nums, k))