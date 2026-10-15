class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        if len(word) > m * n:
            return False

        if sum(row.count(word[0]) for row in board) == 0:
            return False

        if sum(row.count(word[-1]) for row in board) < sum(row.count(word[0]) for row in board):
            word = word[::-1]

        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or r >= m or c < 0 or c >= n
                    or board[r][c] != word[index]):
                return False

            char = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            board[r][c] = char
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False