class Solution(object):
    def compress(self, chars):
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            start = read

            while read < n and chars[read] == char:
                read += 1

            count = read - start
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write