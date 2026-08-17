from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        idx = -1


        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                idx = m
                r = m - 1
            else:
                l = m + 1

       
        if idx != -1 and nums[idx] == target:
            return idx
        return -1



s = Solution()
print(s.search([-1,0,3,5,9,12], target = 9))