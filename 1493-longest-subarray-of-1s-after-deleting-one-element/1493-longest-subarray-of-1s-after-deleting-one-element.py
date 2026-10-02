class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        maximum = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maximum = max(maximum, right - left)

        return maximum