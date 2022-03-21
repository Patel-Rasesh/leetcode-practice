class Solution(object):
    def kClosest(self, points, k):
        return sorted(points, key = lambda point:self.sortEuclidean(point))[:k]
    def sortEuclidean(self, point):
        return pow(pow(point[0], 2)+pow(point[1], 2), 0.5)
obj = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(obj.kClosest(points, k))