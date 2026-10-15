class Solution(object):
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result