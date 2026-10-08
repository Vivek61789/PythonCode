class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for value in gain:
            altitude += value
            highest = max(highest, altitude)

        return highest