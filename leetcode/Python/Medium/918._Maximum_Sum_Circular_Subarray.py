from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        current_max, current_min = 0, 0
        global_max, global_min = nums[0], nums[0]

        ans = 0

        for i in nums:
            current_max = max(current_max + i, i)
            current_min = min(current_min + i, i)
            ans+=i

            global_max = max(global_max, current_max)
            global_min = min(global_min, current_min)

        return max(global_max, ans - global_min) if global_max > 0 else global_max




s = Solution()
print(s.maxSubarraySumCircular([5,-3,5]))