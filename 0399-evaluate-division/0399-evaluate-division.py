from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                current, product = queue.popleft()

                for neighbor, weight in graph[current]:
                    if neighbor in visited:
                        continue

                    new_product = product * weight

                    if neighbor == end:
                        return new_product

                    visited.add(neighbor)
                    queue.append((neighbor, new_product))

            return -1.0

        return [bfs(a, b) for a, b in queries]