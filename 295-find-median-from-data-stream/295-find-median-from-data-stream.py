class MedianFinder(object):

    def __init__(self):
        self.myHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.myHeap.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        
        self.myHeap = sorted(self.myHeap)
        if len(self.myHeap) == 1:
            return self.myHeap[0]
        length = len(self.myHeap)
        if length % 2 == 0:
            return float(self.myHeap[length//2-1] + self.myHeap[length//2])/2
        else:
            return self.myHeap[length//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()