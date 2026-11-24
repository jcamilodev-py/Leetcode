from typing import List
from math import gcd, lcm


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            p = 1
            g = 0
            l = 1

            for j in range(i, n):
                p*=nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if p == g * l:
                    ans = max(ans, (j-i)+1)

        return ans


s = Solution()
print(s.maxLength([1,2,1,2,1,1,1]))