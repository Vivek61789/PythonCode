class Solution(object):
    def findMaxAverage(self, nums, k):
        current = sum(nums[:k])
        maximum = current

        for i in range(k, len(nums)):
            current += nums[i] - nums[i - k]
            maximum = max(maximum, current)

        return float(maximum) / float(k)