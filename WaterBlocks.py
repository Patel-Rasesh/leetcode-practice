class Solution:
    waterBlocks = 0
    waterDict = {}
    #def fillWater(self, subBlock, fill, waterBlocks, waterDict, leftpillar):
    # subBlock - temporary right pillar
    # fill - min height for filling trap
    # waterBlocks - current count of water blocks
    # waterDict - temporary tank - with water block count
    # Leftpillar should not be inclusive
    def fillWater(self, subBlock, fill, leftpillar):
        for rightpillar in range(leftpillar, subBlock):
            if fill - self.waterDict[rightpillar] > 0:
                self.waterBlocks += fill - self.waterDict[rightpillar]
                self.waterDict[rightpillar] = fill
    def trap(self, height):
        # The following approach is analogous to brute-force
        # for key, value in enumerate(height):
        #     self.waterDict[key] = value
        # leftpillar = 0
        # for subBlock in range(len(height)-1):
        #     slope = height[subBlock] - height[subBlock+1]
        #     if(slope < 0):
        #         fill = min(height[leftpillar], height[subBlock+1])
        #         self.fillWater(subBlock+1, fill, leftpillar+1)
        #         # Whichever index is larger, we want that index
        #         if(height[leftpillar] < height[subBlock+1]):
        #             leftpillar = subBlock + 1
        # DP starts from here - 
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for block in range(1, len(height)):
            left_max[block] = max(height[block], left_max[block-1])
        for block in range(len(height)-2, 0, -1):
            right_max[block] = max(height[block], right_max[block+1])
        for block in range(1, len(height)-1):
            self.waterBlocks += min(left_max[block], right_max[block]) - height[block]

# 0 is deleted from height[0]
height = [4,2,0,3,2,5]
# Output: 9
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [5,4,1,2]
obj = Solution()
obj.trap(height)
print("Output ------------------")
print(obj.waterBlocks)
# print(obj.waterDict)
# waterDict = {}
# for key, value in enumerate(height):
#     waterDict[key] = value
# print("Original dict --")
# print(waterDict)
# waterBlocks = 0
# print("-----------------------------")
# waterBlocks, waterDict = obj.fillWater(2, 1, waterBlocks, waterDict, 1)
# print("WaterBlocks = ", waterBlocks)
# print(waterDict)
# print("-----------------------------")
# waterBlocks, waterDict = obj.fillWater(6, 2, waterBlocks, waterDict, 3)
# print("WaterBlocks = ", waterBlocks)
# print(waterDict)
# print("-----------------------------")
# waterBlocks, waterDict = obj.fillWater(9, 2, waterBlocks, waterDict, 7)
# print("WaterBlocks = ", waterBlocks)
# print(waterDict)