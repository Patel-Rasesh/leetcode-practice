class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        iterator = 0
        zeroes = self.countZero(nums)
        while(iterator < len(nums) and zeroes >= 0):
            if nums[iterator] == 0:
                nums.pop(iterator)
                nums.append(0)
                zeroes -= 1
            else:
                iterator += 1
        print(nums)
    def countZero(self, nums):
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
        return zeroes
obj = Solution()
nums = [0,0,1]
obj.moveZeroes(nums)