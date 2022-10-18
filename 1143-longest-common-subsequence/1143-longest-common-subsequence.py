class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # RECURSIVE SOLUTION
        # def LCSRecur(curA, curB):
        #     if curA > m or curB > n:
        #         return 0
        #     ignore = max(LCSRecur(curA+1, curB), LCSRecur(curA, curB+1))
        #     best = ignore
        #     if text1[curA] == text2[curB]:
        #         include = 1 + LCSRecur(curA+1, curB+1)
        #         if include > ignore:
        #             best = include
        #     return best
        # m = len(text1)-1
        # n = len(text2)-1
        # return LCSRecur(0, 0)
        
        DPTable = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        print(DPTable)
        
        for j in reversed(range(len(text2))):
            for i in reversed(range(len(text1))):
                ignore = max(DPTable[i+1][j], DPTable[i][j+1])
                best = ignore
                if text1[i] == text2[j]:
                    include = 1 +DPTable[i+1][j+1]
                    if include > ignore:
                        best = include
                DPTable[i][j] = best
        
        return DPTable[0][0]