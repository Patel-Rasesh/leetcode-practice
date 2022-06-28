class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        myHeap = []
        heapq.heapify(myHeap)
        index = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                index += 1
                heapNode = (-matrix[row][col], -index)
                heapq.heappush(myHeap, heapNode)
                if len(myHeap) > k:
                    heapq.heappop(myHeap)
        return -myHeap[0][0]