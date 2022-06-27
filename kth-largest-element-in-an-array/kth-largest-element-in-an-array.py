import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return list(sorted(nums, reverse=True))[k-1]
        myHeap = []
        heapq.heapify(myHeap)
        for i in range(k):
            heapq.heappush(myHeap, nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] < myHeap[0]:
                continue
            heapq.heappop(myHeap)
            heapq.heappush(myHeap, nums[i])
        
        print(myHeap)
        
        return myHeap[0]