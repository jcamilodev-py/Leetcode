from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0,0

        for i in nums:
            temp = max(i + r1, r2)
            r1 = r2
            r2 = temp
        return r2

s = Solution()
print(s.rob([2,1,1,2]))