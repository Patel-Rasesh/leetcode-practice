import heapq
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
        print(heap)

        return len(heap)
obj = Solution()
#intervals = [[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]
intervals = [[7,10],[2,4]]
print(obj.minMeetingRooms(intervals))