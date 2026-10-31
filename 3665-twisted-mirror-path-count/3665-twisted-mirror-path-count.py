class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # State endpoints: where the robot lands after entering
        # a mirror while moving right (R) or down (D).
        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        # Process backward so each reflected-to mirror is already resolved.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    continue

                # Entered this mirror moving right: reflect down.
                if i + 1 < m:
                    right[i][j] = (
                        down[i + 1][j]
                        if grid[i + 1][j] == 1
                        else (i + 1) * n + j
                    )

                # Entered this mirror moving down: reflect right.
                if j + 1 < n:
                    down[i][j] = (
                        right[i][j + 1]
                        if grid[i][j + 1] == 1
                        else i * n + j + 1
                    )

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0 or grid[i][j] == 1:
                    continue

                ways = dp[i][j]

                # Attempt to move right.
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        dp[i][j + 1] = (dp[i][j + 1] + ways) % MOD
                    else:
                        dest = right[i][j + 1]
                        if dest != -1:
                            r, c = divmod(dest, n)
                            dp[r][c] = (dp[r][c] + ways) % MOD

                # Attempt to move down.
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        dp[i + 1][j] = (dp[i + 1][j] + ways) % MOD
                    else:
                        dest = down[i + 1][j]
                        if dest != -1:
                            r, c = divmod(dest, n)
                            dp[r][c] = (dp[r][c] + ways) % MOD

        return dp[m - 1][n - 1]