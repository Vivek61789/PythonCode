class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                provinces += 1
                stack = [i]
                visited.add(i)

                while stack:
                    city = stack.pop()

                    for neighbor in range(n):
                        if isConnected[city][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

        return provinces