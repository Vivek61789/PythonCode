class Solution(object):
    def minInsertions(self, s):
        open_needed = 0
        insertions = 0

        for char in s:
            if char == '(':
                open_needed += 2

                if open_needed % 2 == 1:
                    insertions += 1
                    open_needed -= 1
            else:
                open_needed -= 1

                if open_needed < 0:
                    insertions += 1
                    open_needed = 1

        return insertions + open_needed