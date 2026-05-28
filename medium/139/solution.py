class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                w_len = len(w)
                if i+w_len>n: continue
                if not dp[i+w_len]: continue
                if s[i:i+w_len] == w:
                    dp[i] = True
                    break

        return dp[0]
