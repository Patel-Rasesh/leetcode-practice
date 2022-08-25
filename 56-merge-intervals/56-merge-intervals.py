class Solution(object):
    def merge(self, intervals):
        # 1. Sort them by starting time
        # intervals.sort(key=lambda x:x[0])
        #bisect.insort(intervals, [2,4])

        # 2. If end time of one interval is overlapping with end time of 
        # subsequent interval, merge them
        # iterator = 0
        # while iterator < len(intervals)-1:
        #     if intervals[iterator][1] >= intervals[iterator+1][0]:
        #         if intervals[iterator][1] >= intervals[iterator+1][1]:
        #             tempInterval = [intervals[iterator][0], intervals[iterator][1]]
        #         else:
        #             tempInterval = [intervals[iterator][0], intervals[iterator+1][1]]
        #         intervals.pop(iterator)
        #         intervals.pop(iterator)
        #         bisect.insort(intervals, tempInterval)
        #     else:
        #         iterator+= 1
        # return intervals
        
        # PRACTICING FOR AMAZON INTERVIEW
        
        def mergeIntervals(interval1, interval2):
            interval = [interval1[0], interval2[1]]
            return interval
        
        # 1. Sort intervals based on their starting time
        intervals = sorted(intervals, reverse = True)
        
        output = []
        
        # 2. Pop from index 0 and check if end time for that popped interval is greater than or 
        # equal to the start time of the next interval (from intervals), merge those intervals
        while len(intervals) >= 2:
            interval1 = intervals.pop(-1)
            interval2 = intervals.pop(-1)
            if interval1[1] >= interval2[0] and interval1[1] >= interval2[1]:
                intervals.append(interval1)
            elif interval1[1] >= interval2[0]:
                intervals.append(mergeIntervals(interval1, interval2))
            
            # 3. Else, append to the final interval list
            else:
                output.append(interval1)
                intervals.append(interval2)
        output.append(intervals[-1])
        
        return output