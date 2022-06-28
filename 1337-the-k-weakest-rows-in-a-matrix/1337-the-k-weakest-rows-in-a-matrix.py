class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Frame a counter (dictionary subclass) using the number of 0's appearing in a 
        # particular row and row's index
        # Return k largest from the heap
        # return heapq.nlargest(k, myHeap,)
        
        # Binary search makes finding weakness more efficient as traversal of the whole 
        # row (of the matrix) is not required
        
        def BS(row):
            low = 0
            high = len(mat[0])
            while low < high:
                mid = low + (high-low) // 2
                if row[mid] == 1:
                    low = mid+1
                else:
                    high = mid
            
            # Returning weakness
            return low
        myHeap = []
        heapq.heapify(myHeap)
        for i, row in enumerate(mat):
            weakness = BS(row)
            heapNode = (-weakness, -i)
            # print(heapNode)
            if len(myHeap) < k or myHeap[0] < heapNode:
                heapq.heappush(myHeap, heapNode)
            if len(myHeap) > k:
                heapq.heappop(myHeap)
    
        # result = sorted(myHeap, key = lambda x:x[0], reverse=True)
        resultIndex = []
        while myHeap:
            _, i = heapq.heappop(myHeap)
            resultIndex.append(-i)
        return resultIndex[::-1]