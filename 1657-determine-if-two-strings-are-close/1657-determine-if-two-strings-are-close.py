class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for char in word1:
            count1[ord(char) - 97] += 1

        for char in word2:
            count2[ord(char) - 97] += 1

        # Both strings must contain the same distinct characters
        if any((count1[i] == 0) != (count2[i] == 0) for i in range(26)):
            return False

        # Frequencies can be rearranged using operation 2
        return sorted(count1) == sorted(count2)