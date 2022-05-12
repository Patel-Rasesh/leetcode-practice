from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        
        sortedNums = sorted(c.items(), key=lambda x:x[1], reverse=True)
        outputArray = []
        
        for index in range(k):
            
            outputArray.append(sortedNums[index][0])
        return outputArray