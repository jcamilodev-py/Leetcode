from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        r = list(range(n+1))

        ans = [0] * n

        for i in range(n):
            if s[i] == "I":
                ans[i] = r[0]
                del r[0]
            else:
                ans[i] = r[-1]
                r.pop()
        return ans + r



s = Solution()
print(s.diStringMatch(s = "III"))