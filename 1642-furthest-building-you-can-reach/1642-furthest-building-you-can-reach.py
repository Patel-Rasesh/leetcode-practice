class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        ladderHeap = []
        for height in range(len(heights)-1):
            climb = heights[height+1] - heights[height]
            if climb <= 0:
                continue
            if len(ladderHeap) < ladders:
                heapq.heappush(ladderHeap, climb)
                continue
            if ladderHeap and climb > ladderHeap[0]:
                bricks -= heapq.heappop(ladderHeap)
                heapq.heappush(ladderHeap, climb)
            else:
                bricks -= climb
            if bricks < 0:
                return height
        return len(heights) -1