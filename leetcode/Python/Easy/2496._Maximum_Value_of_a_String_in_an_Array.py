from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        seen = set({"1","2","3","4","5","6","7","8","9","0"})
        for i in strs:
            alpha = False
            for j in i:
                if j not in seen:
                    ans = max(len(i), ans)
                    alpha = True
                    break
            if not alpha:
                ans = max(int(i), ans)
        return ans


s = Solution()
print(s.maximumValue(["1","01","001","0001"]))