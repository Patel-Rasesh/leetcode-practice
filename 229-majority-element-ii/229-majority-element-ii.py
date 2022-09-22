class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. Find the number of times an element should appear - desiredCount
        desiredCount = round(len(nums)/3 +0.51)
        # 2. Group By similar elements
        nums = Counter(nums)
        # 3. If the length of the grouped by element is more than desiredCount, append that
        #    element to output
        output = set()
        for iterator in nums.elements():
            if nums[iterator] >= desiredCount:
                #if iterator not in output:
                output.add(iterator)
        return output