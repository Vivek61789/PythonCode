class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        removals = 0
        end = intervals[0][1]

        for start, finish in intervals[1:]:
            if start < end:
                removals += 1
            else:
                end = finish

        return removals