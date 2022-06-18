class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_divided_by(n, combinators):
            if combinators == 1:
                return n in squared_nums
            for k in squared_nums:
                if is_divided_by(n-k, combinators-1):
                    return True
            return False
        
        squared_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        # print(squared_nums)
        for combinators in range(1, n+1):
            if is_divided_by(n, combinators):
                return combinators
        
        