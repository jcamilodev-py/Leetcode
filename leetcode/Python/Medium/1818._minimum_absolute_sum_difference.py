from bisect import bisect_left
from typing import List

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        sorted_nums = sorted(nums1)
        total_sum = 0
        max_saving = 0

        for i in range(len(nums1)):
            current_diff = abs(nums1[i] - nums2[i])
            total_sum += current_diff

            target = nums2[i]

            idx = bisect_left(sorted_nums, target)

            best_new_diff = current_diff

            if idx < len(sorted_nums):
                best_new_diff = min(
                    best_new_diff,
                    abs(sorted_nums[idx] - target)
                )

            if idx > 0:
                best_new_diff = min(
                    best_new_diff,
                    abs(sorted_nums[idx - 1] - target)
                )

            saving = current_diff - best_new_diff
            max_saving = max(max_saving, saving)

        return (total_sum - max_saving) % MOD
                



s = Solution()
print(s.minAbsoluteSumDiff([1,7,5], nums2 = [2,3,5]))