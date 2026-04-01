from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(indices)
        for i,j in zip(s, indices):
            ans[j] = i

        return "".join(ans)       

s = Solution()
print(s.restoreString("abc",[2,1,0]))