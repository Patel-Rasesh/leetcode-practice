class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda point:self.sortEuclidean(point))[:k]
    def sortEuclidean(self, point):
        return pow(pow(point[0], 2)+pow(point[1], 2), 0.5)