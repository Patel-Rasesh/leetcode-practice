class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if upper == lower:
            return [upper]
        if len(nums) == 0:
            # TODO 
            # When lower is present, when upper is present and when both are present
            if not lower and not upper:
                return []
            elif not lower:
                return [upper]
            elif not upper:
                return [lower]
            else:
                return[str(lower)+'->'+str(upper)]
        output = []
        stringOutput = []
        if lower > nums[0]:
            print("Lower should be smaller than index 0 of nums")
        elif lower <= nums[0]:
            if nums[0] - lower >= 1:
                output.append([lower, nums[0]-1])
        for num in range(len(nums)-1):
            if (nums[num+1] - nums[num]) >= 2:
                output.append([nums[num]+1, nums[num+1]-1])
        if upper < nums[-1]:
            print("Upper should be larger than index -1 of nums")
        else:
            if upper - nums[-1] >= 2:
                output.append([nums[-1]+1, upper])
        for subArray in output:
            if subArray[1] - subArray[0] > 0:
                tempString = str(subArray[0])+"->"+str(subArray[1])
                stringOutput.append(tempString)
            else:
                stringOutput.append(str(subArray[0]))
        return stringOutput
obj = Solution()
nums = [-1]
low = -1
high = -1
print(obj.findMissingRanges(nums, low, high))
