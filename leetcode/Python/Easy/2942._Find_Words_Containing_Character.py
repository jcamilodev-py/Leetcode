from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        ans = []

        for i in range(n):
            if x in set(words[i]):
                ans.append(i)
        return ans




s = Solution()
print(s.findWordsContaining(["abc","bcd","aaaa","cbc"], x = "a"))