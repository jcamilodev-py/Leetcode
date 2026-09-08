from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for w in wordDict:
                j = i - len(w)
                if j >= 0:
                    if s[j:i] == w and dp[j] == True:
                        dp[i] = True

        return dp[-1]






s = Solution()
print(s.wordBreak(s = "aab", wordDict = ["ab","a"]))