class Solution(object):
    def decodeString(self, s):
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0

            elif char == ']':
                previous_str, repeat = stack.pop()
                current_str = previous_str + current_str * repeat

            else:
                current_str += char

        return current_str