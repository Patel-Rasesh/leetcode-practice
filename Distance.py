import numpy as np
import math
import heapq

a = np.array([[2, 2], [3, 4], [5, 5], [6, 7], [9, 12], [1, 2], [9, 2]])
#a = np.array([1, 2, 4, 3])

#a = np.array([[0,1],[1,0]])
def squared_distance(a):
     return a[0] ** 2 + a[1] ** 2
b = sorted(a, key = squared_distance)
print(b[:3])
# for i in range(len(a)):
#     dist.append(np.sqrt(np.add(pow(a[i][0], 2), pow(a[i][1], 2))))

# print(a)
# print(dist)
# sortedDist = heapq.nsmallest(2, dist)
# print(sortedDist)
# output = [[0, 0]] * 2
# flag = True

# for i in range(len(sortedDist)):
#     for j in range(len(dist)):
#         flag = True
#         if(sortedDist[i] == dist[j]):
#             for z in range(len(output)):
#                 if(output[z][0] == a[j][0] and (output[z][1] == a[j][1])):
#                     flag = False
#             if(flag == True):
#                 output[i] = [a[j][0], a[j][1]]
# print(output)