class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        result = ['']

        for digit in digits:
            result = [
                combination + char
                for combination in result
                for char in phone[digit]
            ]

        return result