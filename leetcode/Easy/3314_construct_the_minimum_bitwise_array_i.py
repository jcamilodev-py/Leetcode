from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            x = 0
            while x <= i:
                if x | (x + 1) == i:
                    ans.append(x)
                    break
                x+=1
                if x > i:
                    ans.append(-1)
        return ans


s = Solution()
print(s.minBitwiseArray([2,7]))