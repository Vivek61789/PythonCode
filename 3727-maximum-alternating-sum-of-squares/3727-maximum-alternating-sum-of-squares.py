class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = sorted(x * x for x in nums)
        mid = len(squares) // 2

        return sum(squares[mid:]) - sum(squares[:mid])