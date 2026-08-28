from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)

        mod = 10 ** 9 + 7


        p = [0] * (n+1)

        for i in range(1, n+1):
            p[i] = p[i-1] + nums[i-1]

        ans = 0

        for i in range(1, n-1):
            l = bisect_left(p, 2*p[i], i+1, n)
            h = bisect_right(p, (p[n] + p[i]) // 2, i+1, n) - 1

            if l <= h:
                ans+=h - l + 1

        return ans % mod


s = Solution()
print(s.waysToSplit([7,2,5,5,6,2,10,9]))