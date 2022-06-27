class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return stones[0]
        
        # Making it ready for max-heap
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while(len(stones)) > 1:
            stoneOne, stoneTwo = heapq.heappop(stones), heapq.heappop(stones)
            if stoneOne != stoneTwo:
                heapq.heappush(stones, -(stoneTwo-stoneOne))
                
        if stones:
            return heapq.heappop(stones)*-1
        else:
            return 0
        