from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for i in sentences:
            n = len(i.split())
            if n > ans:
                ans = n
        return ans




s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))