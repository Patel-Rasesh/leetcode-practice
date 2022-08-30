class Solution(object):
    def minMeetingRooms(self, intervals):
#         if not intervals:
#             return 0
        
#         #return sorted(intervals, key= lambda  x:x[1])
#         sortedIntervals = sorted(intervals)
        
#         heap = []
#         heapq.heapify(heap)
#         heapq.heappush(heap, sortedIntervals[0][1])
#         for intervalIndex in range(1,len(sortedIntervals)):
#             if sortedIntervals[intervalIndex][0] >= heap[0]:
#                 heapq.heappop(heap)
#             heapq.heappush(heap,sortedIntervals[intervalIndex][1])

#         return len(heap)

        # AMAZON INTERVIEW PREP
        
        # 1. Compare start time of new interval with the end time stored in the minheap
        heap = []
        heapq.heapify(heap)
    
        intervals = sorted(intervals)
        
        heapq.heappush(heap, intervals[0][1])
        intervals.pop(0)
        
        # 2. If start time is greater than the priority node's end time, pop prioirty node and push the new interval
        while len(intervals) != 0:
            # tempNode = heapq.heappop(heap)
            # if tempNode > intervals[0][0]:
            if intervals[0][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[0][1])
            intervals.pop(0)
    
        # 4. Return the length of the min heap
        return len(heap)