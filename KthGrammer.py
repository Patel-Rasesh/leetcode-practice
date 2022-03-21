class Solution(object):
    def flip(self, n, flippedResultTable):
        if not n:
            return flippedResultTable
        tempTable = flippedResultTable
        for charac in tempTable:
            if (charac == '0'):
                flippedResultTable += '1'
            else:
                flippedResultTable += '0'
        n -= 1
        return self.flip(n, flippedResultTable)
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if(n == 1):
            return "0"
        if(n == 2):
            tempString = "01"
            return tempString[k-1]
        finalString = self.flip(n-2, "01")
        return finalString[k-1]
        
        