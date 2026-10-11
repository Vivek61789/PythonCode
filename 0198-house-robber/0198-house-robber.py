class Solution(object):
    def rob(self, nums):
        prev2 = 0
        prev1 = 0

        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1