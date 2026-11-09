import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        # Segment tree: 1 means available, 0 means busy.
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Find the first available server with index >= start.
        def find(node, left, right, start):
            if right < start or tree[node] == 0:
                return -1

            if left == right:
                return left if left < k else -1

            mid = (left + right) // 2

            result = find(node * 2, left, mid, start)

            if result != -1:
                return result

            return find(node * 2 + 1, mid + 1, right, start)

        # Update server availability.
        def update(index, available):
            pos = size + index
            tree[pos] = available

            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        busy = []
        handled = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            # Release servers whose requests have finished.
            while busy and busy[0][0] <= current_time:
                finish_time, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            # Find the next available server.
            server = find(1, 0, size - 1, start)

            # Wrap around if necessary.
            if server == -1:
                server = find(1, 0, size - 1, 0)

            if server == -1:
                continue

            handled[server] += 1
            update(server, 0)

            heapq.heappush(
                busy,
                (current_time + load[i], server)
            )

        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]