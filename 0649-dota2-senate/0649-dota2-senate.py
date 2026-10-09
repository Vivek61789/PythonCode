from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"