class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # return sorted(points, key = lambda point:self.sortEuclidean(point))[:k]
#         myHeap = []
#         heapq.heapify(myHeap)
#         for index, point in enumerate(points):
#             distance = self.sortEuclidean(point)
#             heapNode = (-distance, index)
#             heapq.heappush(myHeap, heapNode)
#             if len(myHeap) > k:
#                 heapq.heappop(myHeap)
#         print(myHeap)
        
#         closestPoints = []
#         while myHeap:
#             index = heapq.heappop(myHeap)[1]
#             closestPoints.append(points[index])
        
#         return closestPoints
    
#     def sortEuclidean(self, point):
#         return pow(pow(point[0], 2)+pow(point[1], 2), 0.5)

        
        # AMAZON INTERVIEW PREP
        
        def EuclideanDistance(point):
            return pow(point[1], 2)+ pow(point[0], 2)
        
        return sorted(points, key= lambda point: EuclideanDistance(point))[:k]