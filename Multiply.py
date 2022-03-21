class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return int(num1) * int(num2)

obj = Solution()
num1 = "123"
num2 = "456"
print(obj.multiply(num1, num2))