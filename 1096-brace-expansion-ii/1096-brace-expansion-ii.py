class Solution(object):
    def braceExpansionII(self, expression):
        def parse(pos):
            result = set()
            current = {""}

            while pos[0] < len(expression) and expression[pos[0]] != '}':
                ch = expression[pos[0]]

                if ch == ',':
                    result.update(current)
                    current = {""}
                    pos[0] += 1

                elif ch == '{':
                    pos[0] += 1
                    group = parse(pos)
                    pos[0] += 1

                    current = {a + b for a in current for b in group}

                else:
                    current = {a + ch for a in current}
                    pos[0] += 1

            result.update(current)
            return result

        pos = [0]
        return sorted(parse(pos))