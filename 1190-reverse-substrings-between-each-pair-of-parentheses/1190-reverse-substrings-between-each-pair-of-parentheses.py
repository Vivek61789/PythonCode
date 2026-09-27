class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                text = stack.pop()
                text.reverse()

                if stack:
                    stack[-1].extend(text)
                else:
                    stack.append(text)
            else:
                if not stack:
                    stack.append([])
                stack[-1].append(ch)

        return ''.join(stack[0])