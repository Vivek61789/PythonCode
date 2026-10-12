class Solution(object):
    def longestZigZag(self, root):
        self.max_length = 0

        def dfs(node, left, right):
            if not node:
                return

            self.max_length = max(self.max_length, left, right)

            dfs(node.left, right + 1, 0)
            dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.max_length