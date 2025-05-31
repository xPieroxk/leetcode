from collections import defaultdict
from collections import Counter


class Solution:
    def minWindow(self, s, t):
        freq_t = Counter(t)
        freq_window = defaultdict(int)
        have, need = 0, len(freq_t)

        res = [float('inf'), 0, 0]
        l = 0

        for r, c in enumerate(s):
            freq_window[c] += 1

            if c in freq_t and freq_window[c] == freq_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]

                freq_window[s[l]] -= 1
                if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res[1], res[2]
        return s[l:r + 1] if res[0] != float('inf') else ""
