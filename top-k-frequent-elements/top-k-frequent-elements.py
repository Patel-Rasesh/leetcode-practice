from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)        
        return heapq.nlargest(k, c.keys(), key=c.get)
        
        # sortedNums = sorted(c.items(), key=lambda x:x[1], reverse=True)
        # outputArray = []
        
        
        # for index in range(k):
        #     outputArray.append(sortedNums[index][0])
        # return outputArray
        