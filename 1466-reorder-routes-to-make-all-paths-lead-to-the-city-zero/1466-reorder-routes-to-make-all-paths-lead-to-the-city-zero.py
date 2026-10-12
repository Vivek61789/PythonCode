from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = {0}
        queue = deque([0])
        changes = 0

        while queue:
            city = queue.popleft()

            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += cost
                    queue.append(neighbor)

        return changes