from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        k = len(pref)
        ans = 0

        for i in words:
            if i[:k] == pref:
                ans+=1

        return ans




s = Solution()
print(s.prefixCount(["leetcode","win","loops","success"], pref = "code"))