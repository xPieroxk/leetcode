from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in s:
            freq1[c] = freq1[c] + 1

        for c in t:
            freq2[c] = freq2[c] + 1

        return freq1 == freq2
