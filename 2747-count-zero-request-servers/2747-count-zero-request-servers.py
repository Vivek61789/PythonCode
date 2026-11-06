class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        indexed_queries = sorted(
            (time, i) for i, time in enumerate(queries)
        )

        freq = [0] * (n + 1)
        active = 0
        left = right = 0
        ans = [0] * len(queries)

        for time, idx in indexed_queries:
            start = time - x

            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans