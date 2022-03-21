class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
       # Min of computeWages is the answer
        computedWages = []
        for baseIndex, baseWage in enumerate(wage):
            for variableIndex, variableWage in enumerate(wage):
                if baseWage == variableWage:
                    continue
                # Find the relation between 
                # quality[baseIndex] and quality[variableIndex]
                ratio = quality[variableIndex]/quality[baseIndex]
                tempWage = 0
                if ratio*baseWage >= variableWage:
                    tempWage = ratio*baseWage
                    computedWages.append(tempWage)
        print(sorted(computedWages))
        return sum(sorted(computedWages)[:k])

obj = Solution()
#quality = [3,1,10,10,1]
quality = [10,20,5]
#wages = [4,8,2,2,7]
wages = [70,50,30]
k = 2
print(obj.mincostToHireWorkers(quality, wages, k))