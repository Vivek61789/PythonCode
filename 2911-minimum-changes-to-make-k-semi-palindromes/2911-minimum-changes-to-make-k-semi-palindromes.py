class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome.
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Try every proper divisor of the substring length.
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare mirrored characters in each group.
                    for offset in range(d):
                        left = i + offset
                        right = j - ((length - 1 - offset) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # dp[p][i] = minimum changes to partition first i characters
        # into exactly p semi-palindromes.
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    if dp[parts - 1][start] != INF:
                        dp[parts][end] = min(
                            dp[parts][end],
                            dp[parts - 1][start] + cost[start][end - 1]
                        )

        return dp[k][n]