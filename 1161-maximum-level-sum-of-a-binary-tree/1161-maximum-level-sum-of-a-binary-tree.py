from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        best_level = 1
        max_sum = float('-inf')

        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level

            level += 1

        return best_level