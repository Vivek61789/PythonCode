class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        digits = []
        for _ in range(num):
            digit = min(9, sum)
            digits.append(str(digit))
            sum -= digit

        if sum > 0:
            return ""

        return "".join(digits)