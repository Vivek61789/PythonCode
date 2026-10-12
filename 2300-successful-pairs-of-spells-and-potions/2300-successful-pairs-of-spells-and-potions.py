class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            left, right = 0, m

            while left < right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            result.append(m - left)

        return result