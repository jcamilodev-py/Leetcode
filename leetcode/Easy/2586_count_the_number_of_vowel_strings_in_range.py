from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        seen = set({'a', 'e', 'i', 'o','u'})
        for i in range(left, right+1):
            if words[i][0] in seen and words[i][-1] in seen:
                ans+=1
        return ans
            


s = Solution()
print(s.vowelStrings(["are","amy","u"], left = 0, right = 2))