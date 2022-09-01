class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        score = [0] * len(nums)
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (-nums[0], 0))
        score[0] = nums[0]
        for index in range(1, len(nums)):
            while heap[0][1] < index-k:
                heapq.heappop(heap)
            score[index] = nums[index] + score[heap[0][1]]
            heapq.heappush(heap, (-score[index], index))
        
        return score[-1]