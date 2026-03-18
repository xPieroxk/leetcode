from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_l = len(s1)
        s2_l = len(s2)
        if s1_l > s2_l:
            return False

        s1_counts = defaultdict(int)
        window_counts = defaultdict(int)
        for i in range(s1_l):
            s1_counts[s1[i]] += 1
            window_counts[s2[i]] += 1

        for i in range(s1_l, s2_l):
            if s1_counts == window_counts:
                return True
            window_counts[s2[i]] += 1
            window_counts[s2[i - s1_l]] -= 1
            if window_counts[s2[i - s1_l]] == 0:
                del window_counts[s2[i - s1_l]]

        return s1_counts == window_counts
