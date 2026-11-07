import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)

        busy = []  # (finish_time, weight, server_index)
        ans = [0] * len(tasks)
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release every server that has become available.
            while busy and busy[0][0] <= time:
                _, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

            # If no server is free, jump to the earliest finish time.
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    _, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))

            weight, index = heapq.heappop(free)
            ans[i] = index

            heapq.heappush(
                busy,
                (time + duration, weight, index)
            )

        return ans