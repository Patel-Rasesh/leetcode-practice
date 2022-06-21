class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # Brute Force - Time Limit Expiration
#         warmDays = []
#         for temp1 in range(len(temperatures)):
#             change = False
#             for temp2 in range(temp1, len(temperatures)):
                
#                 # We can remember values (temperatures) while traversing
#                 # this, and call immediate warmer days from the stack (approach 2)
#                 if temperatures[temp2] > temperatures[temp1]:
#                     change = True
#                     warmDays.append(temp2-temp1)
#                     break
#             if change == False:
#                 warmDays.append(0)
        
#         # warmDays.append(0)
#         return warmDays

        # Approach 2 - using monotonic (decreasing) stack
        warmDays = [0] * len(temperatures)
        stackTemp = []
        stackTemp.append(0)
        for eachDay in range(1, len(temperatures)):
            count = 0
            while stackTemp and temperatures[eachDay] > temperatures[stackTemp[-1]]:
                count += 1
                warmDays[stackTemp[-1]] = eachDay - stackTemp[-1]
                stackTemp.pop(-1)
            stackTemp.append(eachDay)
        return warmDays