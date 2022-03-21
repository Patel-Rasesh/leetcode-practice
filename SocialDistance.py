# Veteran's united Web developer coding test
# Concatenate strings for maximum length
# #master = ["potato", "kayak", "banana", "racecar"]
# master = ["eva", "jqw", "tyn", "jan"]
# masterSetList = []
# for slave in master:        
#     masterSetList.append(set(list(slave)))

# def lengthOfString(word):
#     return len(word)
# masterSetList.sort(key=lengthOfString, reverse=True)
# print(len(masterSetList[0]) + len(masterSetList[1]))

# # master = ["potato", "kayak", "banana", "racecar"]
# master = ["eva", "jqw", "tyn", "jan"]

# # def lengthOfString(word):
# #     return len(word)
# masterSetList = []

# for word in master:
#     if (len(word) != len(set(list(word)))):
#         continue
#     masterSetList.append(len(word))

# masterSetList.sort(reverse=True)
# print(masterSetList)

class Solution(object):
    def findNextOne(self, seats, index):
        if(seats[index] == 1):
            return index
        if(index == len(seats) - 1):
            return index
        return self.findNextOne(seats, index+1)
    
    def findDifference(self, segment):
        return segment[1]-segment[0]
        
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        segments = []
        start = 0
        while(start != len(seats)-1):
            if seats[start] == 0:
                nextOne = self.findNextOne(seats, start)
                if(nextOne == len(seats)-1) and seats[nextOne] == 0:
                    segments.append([start, nextOne])
                else:
                    segments.append([start, nextOne-1])
                start = nextOne
            else:
                start += 1
        segments.sort(key=self.findDifference, reverse=True)
        if(segments[0][1] == len(seats)-1):
            return segments[0][1]
        return int((segments[0][1] + segments[0][0])/2)

seats = [0,1]
obj = Solution()
print(obj.maxDistToClosest(seats))