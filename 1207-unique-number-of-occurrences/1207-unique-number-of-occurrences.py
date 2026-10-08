class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = {}

        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        return len(counts) == len(set(counts.values()))