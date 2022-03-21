import numpy as np
from typing import DefaultDict
from collections import defaultdict

arr = np.array([-1, -2, 3, 4])
# print(heapq.nlargest(12, arr)[-1])
countDict = defaultdict(int)

for i in range(len(arr)):
    countDict[arr[i]] += 1

print(countDict)

arrangedOutput = []
arrangedOutput.append(4)
countDict[4] -= 1

print(countDict)