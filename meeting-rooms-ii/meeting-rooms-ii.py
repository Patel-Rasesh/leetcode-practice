class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        #return sorted(intervals, key= lambda  x:x[1])
        sortedIntervals = sorted(intervals)
        
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, sortedIntervals[0][1])
        for intervalIndex in range(1,len(sortedIntervals)):
            if sortedIntervals[intervalIndex][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,sortedIntervals[intervalIndex][1])

        return len(heap)