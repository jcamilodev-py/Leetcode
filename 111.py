from typing import List

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        v1 = sum(nums[len(nums)-k:len(nums)])
        v2 = sum(nums[0:k])
        return abs(v1 - v2)


s = Solution()
print(s.absDifference([100], 1))