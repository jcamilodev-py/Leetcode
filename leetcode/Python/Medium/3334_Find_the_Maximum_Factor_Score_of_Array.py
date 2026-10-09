from typing import List
from math import gcd, lcm


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        pg = [0] * (n+1)
        pl = [1] * (n+1)

        sg = [0] * (n+1)
        sl = [1] * (n+1)

        for i in range(n):
            pg[i+1] = gcd(pg[i], nums[i])
            pl[i+1] = lcm(pl[i], nums[i])


        for i in range(n-1, -1, -1):
            sg[i] = gcd(sg[i+1], nums[i])
            sl[i] = lcm(sl[i+1], nums[i])

        ans = pg[n] * pl[n]

        for i in range(n):
            ans = max(ans, gcd(pg[i], sg[i+1]) * lcm(pl[i], sl[i+1]))

        return ans



s = Solution()
print(s.maxScore([2,4,8,16]))