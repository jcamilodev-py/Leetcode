from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)




s = Solution()
print(s.searchInsert([1,3,5,6], target = 5))