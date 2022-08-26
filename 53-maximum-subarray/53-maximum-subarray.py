class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         maxSubarray = -math.inf
#         for i in range(len(nums)):
#             localSum = 0
#             for j in range(i, len(nums)):
#                 localSum += nums[j]
#                 maxSubarray = max(localSum, maxSubarray)
        
#         return maxSubarray

        current_subarray = nums[0]
        max_subarray = nums[0]

        for j in range(1, len(nums)):
            current_subarray = max(current_subarray+nums[j], nums[j])
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray
                