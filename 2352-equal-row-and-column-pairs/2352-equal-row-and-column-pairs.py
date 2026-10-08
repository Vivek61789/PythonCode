class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)

        rows = {}
        for row in grid:
            key = tuple(row)
            rows[key] = rows.get(key, 0) + 1

        answer = 0

        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            answer += rows.get(column, 0)

        return answer