class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
#         # 1. Sort events by their end time
#         events = sorted(events, key = lambda x:x[1])
#         print(events)
        
#         # 2. Make a list of days and set each day as 0
#         days = [0] * events[-1][1]
#         days.append(0)
        
#         # 3. Mark a day 1 as you can accomodate them traversing events
#         canAttend = 0
#         for event in events:
#             [start, end] = event
#             for i in range(start, end+1):
#                 if days[i] == 0:
#                     days[i] = 1
#                     canAttend += 1
#                     break
            
#         print(days)  # Sanity check
        
#         # 4. Return the total events that can be attended
#         return canAttend

        # AMAZON INTERVIEW PREP    
    
        events = sorted(events)
        total_days = max(events, key = lambda x:x[1])[1]
        day = events[0][0]
        withinDay = 0
        count = 0
        
        heap = []
        heapq.heapify(heap)
        
        # 1. Day increases to the end day of the last event
        while day <= total_days:
        
            # 2. Add events to the heap as their respective day arrives
            while withinDay < len(events) and events[withinDay][0] <= day:
                heapq.heappush(heap, events[withinDay][1])
                withinDay += 1
            
            # 3. Pop events from heap as their end time elapse
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # 4. Increase count if event is still in the heap
            if heap:
                heapq.heappop(heap)
                count += 1
            
            day += 1
            
        return count