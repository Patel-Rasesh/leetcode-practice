class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
#         heapq.heapify(sticks)
#         totalCost = 0
        
#         while len(sticks) > 1:
#             stick1 = heapq.heappop(sticks)
#             stick2 = heapq.heappop(sticks)
#             heapq.heappush(sticks, stick1+stick2)
#             totalCost += stick1+stick2
        
#         return totalCost
        
    
        # AMAZON INTERVIEW PREP
        
        if len(sticks) == 1:
            return 0
        heapq.heapify(sticks)
        totalCost = 0
        
        while len(sticks) > 1:
            localCost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, localCost)
            totalCost += localCost 
        
        return totalCost