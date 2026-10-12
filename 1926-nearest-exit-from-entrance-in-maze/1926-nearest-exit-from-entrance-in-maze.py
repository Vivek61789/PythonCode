from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        r, c = entrance

        queue = deque([(r, c, 0)])
        maze[r][c] = '+'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, steps = queue.popleft()

            if steps > 0 and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                        and maze[nr][nc] == '.'):
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))

        return -1