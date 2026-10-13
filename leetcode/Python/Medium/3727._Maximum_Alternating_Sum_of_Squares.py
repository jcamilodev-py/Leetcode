from typing import List
from math import ceil


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        nums = [abs(i) for i in nums]
        nums.sort(reverse=True)
        even = sum(i**2 for i in nums[:ceil(n/2)])
        odd = sum(i**2 for i in nums[ceil(n/2):])

        return even - odd


s = Solution()
print(s.maxAlternatingSum([-3,-1,-2,3,2,1]))