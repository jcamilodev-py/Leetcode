from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0


        n = len(nums)

        for i in range(n):
            bl = bisect_left(nums, lower - nums[i], i+1, n)
            br = bisect_right(nums, upper - nums[i], i+1, n)

            ans+= br - bl

        return ans




s = Solution()
print(s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))