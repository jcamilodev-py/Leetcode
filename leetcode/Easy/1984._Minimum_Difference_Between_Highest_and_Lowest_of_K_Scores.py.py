from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        ans = float('inf')
        while i <= n - k:
            ans = min(ans, nums[i + k - 1] - nums[i])
            i+=1
        
        return ans



s = Solution()
print(s.minimumDifference([87063,61094,44530,21297,95857,93551,9918], k = 6))