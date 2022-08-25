class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # 1. Sort boxTypes using unitSize
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        print(boxTypes)
        
        # 2. Start fitting boxes from the front until the truckSize if reached
        weight = 0
        for box in boxTypes:
            for eachBox in range(box[0]):
                truckSize -= 1
                weight += box[1]
                if truckSize == 0:
                    return weight
         
        return weight