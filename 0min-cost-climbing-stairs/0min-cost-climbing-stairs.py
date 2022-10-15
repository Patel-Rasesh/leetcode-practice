class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 0. Recursive formula
        # Input: cost = [1,100,1,1,1,100,1,1,100,1]
        # Base cases
        # f(0) = cost[0]
        # f(1) = cost[1]
        # f(n) = min(f(n-1), f(n-2))+cost[n]
        
        def minCostRecur(n):
            if n==0:
                return cost[0]
            if n==1:
                return cost[1]
            if memo[n] is None:
                memo[n] = min(minCostRecur(n-1), minCostRecur(n-2))+cost[n]
            return memo[n]
        
        memo = [None]*(len(cost)+1)
        print(memo)
        cost.append(0)
        print(cost)
        return minCostRecur(len(cost)-1)