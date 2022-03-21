from collections import defaultdict

import numpy as np
trust = np.array([[1,3],[1,4],[2,3],[2,4],[4,3]])
inDegree = defaultdict(int)
outDegree = defaultdict(int)

def findJudge(trust, n):
    for x, y in trust:
        inDegree[y] += 1 
        outDegree[x] += 1

    for i in range(1, n+1):
        if(inDegree[i] == n and outDegree[i] == 0):
            return i
    return -1 
print(findJudge(trust, 3))


    