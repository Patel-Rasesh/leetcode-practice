class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)-1
        n = len(text2)-1
        
#         Recursive solution - TLE
#         def LCSrecur(i, j):
#             if i > m or j > n:
#                 return 0
#             ignore = max(LCSrecur(i+1, j), LCSrecur(i, j+1))
#             best = ignore
#             if text1[i] == text2[j]:
#                 include = 1 + LCSrecur(i+1, j+1)
#                 if include > best:
#                     best = include
#             return best
        
#         return LCSrecur(0, 0)
        
        # DP solution
        def LCSDP():
            # 1. Frame a 2D array, (x,y) both decreasing, and initialize with base cases
            table = [[0] * (n+2) for _ in range(m+2)]
            # table = [[0] * (n+2)]*(m+2)
            
            # 2. Two for loops to iterate through the table (2D array) and fill the table entries up
            for i in reversed(range(m+1)):
                for j in reversed(range(n+1)):
               
                    # 3. Rest of the code is same, only replace table entries in place of recursive calls
                    ignore = max(table[i+1][j], table[i][j+1])
                    best = ignore
                    if text1[i] == text2[j]:
                        include = 1 + table[i+1][j+1]
                        if include > best:
                            best = include
                    table[i][j] = best
                    
            return table[0][0]    
        return LCSDP()
        