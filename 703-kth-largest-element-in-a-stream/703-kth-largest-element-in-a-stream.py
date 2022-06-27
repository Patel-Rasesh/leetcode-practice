class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.myHeap = nums
        self.k = k
        heapq.heapify(self.myHeap)
        while len(self.myHeap) > k:
            heapq.heappop(self.myHeap)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
    
        heapq.heappush(self.myHeap, val)
        if len(self.myHeap) > self.k:
            heapq.heappop(self.myHeap)
        return self.myHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)