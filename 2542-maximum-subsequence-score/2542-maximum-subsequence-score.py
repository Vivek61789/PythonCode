import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        total = 0
        result = 0

        for num2, num1 in pairs:
            heapq.heappush(heap, num1)
            total += num1

            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                result = max(result, total * num2)

        return result