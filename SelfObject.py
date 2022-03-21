class Solution:
    localVariable = 10
    def temporary(self):
        print("Inside the function")

obj = Solution
obj.temporary
print(obj.localVariable)
