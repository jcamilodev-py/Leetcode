from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        r = 0

        for i in nums:
            if i == 0:
                r+=1
                ans+=r
            else:
                r = 0

        return ans



s = Solution()
print(s.zeroFilledSubarray([0,0,0,2,0,0]))