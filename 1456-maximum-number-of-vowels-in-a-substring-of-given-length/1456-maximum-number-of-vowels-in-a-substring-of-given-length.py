class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")

        count = sum(c in vowels for c in s[:k])
        maximum = count

        for i in range(k, len(s)):
            count += s[i] in vowels
            count -= s[i - k] in vowels
            maximum = max(maximum, count)

        return maximum