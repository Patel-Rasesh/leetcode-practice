class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        
        print(horizontalCuts)
        print(verticalCuts)
        
        cutHSpace = 0
        for eachCut in range(len(horizontalCuts)-1):
            if horizontalCuts[eachCut+1]-horizontalCuts[eachCut] > cutHSpace:
                cutHSpace = horizontalCuts[eachCut+1]-horizontalCuts[eachCut]
        
        cutVSpace = 0
        for eachCut in range(len(verticalCuts)-1):
            if verticalCuts[eachCut+1]-verticalCuts[eachCut] > cutVSpace:
                cutVSpace = verticalCuts[eachCut+1]-verticalCuts[eachCut]
        
        return (cutHSpace*cutVSpace)%(pow(10,9)+7)