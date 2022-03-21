class Solution(object):
    def twoSum(self, numbers, target):
        for i, iterator in enumerate(numbers):
            if (target-iterator) in numbers:
                if iterator != target-iterator:
                    return sorted((i+1, numbers.index(target-iterator)+1))
                else:
                    return [i+1, i+2]

obj = Solution()
numbers = [1,2,3,4,4,9,56,90]
target = 8
print(obj.twoSum(numbers, target))