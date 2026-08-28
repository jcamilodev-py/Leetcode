from typing import List
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        n = len(nums)
        return False if bisect_left(nums, target) == n or nums[bisect_left(nums, target)] != target else True




s = Solution()
print(s.search([2,5,6,0,0,1,2], target = 3))