class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        iterator = 0
        while iterator < len(nums)-1:
            if nums[iterator] == nums[iterator+1]:
                nums.pop(iterator)
            else:
                iterator += 1
        print(nums)

obj = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
obj.removeDuplicates(nums)