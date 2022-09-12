class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. Declare two pointers (left, right) and maxWater 
        left, right = 0, len(height)-1
        maxWater = 0
        
        # 2. Calculating the water it can hold with that width (right-left)
        def calWater(left, right):
            return (right-left)*min(height[left], height[right])
        
        # 3. Base condition is when right = left
        while left < right:
            if calWater(left, right) > maxWater:
                # 4. Update the maxWater
                maxWater = calWater(left, right)
            
            # 3. Drop the min column, and increment that pointer
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1    
        
        return maxWater