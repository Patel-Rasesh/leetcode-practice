class Solution(object):
    def findDivisorFunction(self, divisor, k):
        if divisor%k == 0:
            return len(str(divisor))
        divisor = (divisor * 10) + 1
        return self.findDivisorFunction(divisor, k)

divisor = Solution()
print("Length of the divisor = ", divisor.findDivisorFunction(1, 3))