class Solution(object):
    def maxDepthAfterSplit(self, seq):
        depth = 0
        answer = []

        for char in seq:
            if char == '(':
                depth += 1
                answer.append(depth & 1)
            else:
                answer.append(depth & 1)
                depth -= 1

        return answer