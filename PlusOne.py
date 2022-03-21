class Solution:
    def plusOne(self, digits):
        if digits[-1] == 9:
            digits[-1] = 0
            digits[-2] += 1
        else:
            digits[-1] += 1
        return digits

obj = Solution()
digits = [9]
print(obj.plusOne(digits))