from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        # nums = []
        # for num in range(1,n+1):
        #     nums.append(num)
        # intermediate = []
        # output = [[]]
        # for num in nums:
        #     output += [curr + [num] for curr in output]
        # index = 0
        # while (index < len(output)):
        #     if len(output[index]) != k:
        #         output.pop(index)
        #     else:
        #         index += 1
        # return output
        #tempOutput = []
        # for index in range(n+1):
        output = [[]]
        for element in range(n):
            output.append(self.iterComb(n, element))
            # output.append(tempOutput)
        return output
    def iterComb(self, n, k):
        return list(combinations([i for i in range(1, n+1)], k))

obj = Solution()
n = 1
k = 1
print(obj.combine(n, k))