from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)

        l=0
        m_lenght = 0
        for r in range(len(s)):
            freqs[s[r]]+=1
            curr_max_freq = max(freqs.values())

            while (r-l+1)-curr_max_freq>k:
                freqs[s[l]] -=1
                l+=1
                curr_max_freq = max(freqs.values())
            m_lenght = max(m_lenght,r-l+1)

        return m_lenght


# Less intuitive solution where the max freq is global.
# In this solution the windows 'slides' with the same width and ONLY when a new max_freq is found the m_lenght
# increases. Both solution are O(n) since letters in the alph are 26 the max function is constant on max(freqs.values())

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)

        l=0
        m_lenght = 0
        max_freq = 0
        for r in range(len(s)):
            freqs[s[r]]+=1
            max_freq = max(max_freq, freqs[s[r]])

            while (r-l+1)-max_freq>k:
                freqs[s[l]] -=1
                l+=1

            m_lenght = max(m_lenght,r-l+1)

        return m_lenght