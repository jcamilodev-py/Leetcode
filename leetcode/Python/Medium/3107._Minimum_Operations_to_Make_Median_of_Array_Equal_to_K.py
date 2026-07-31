from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        ans+=abs(nums[n // 2] - k)

        nums[n // 2] = k

        for i in range(n // 2):
            if nums[n // 2] < nums[i]:
                ans+=abs(nums[n // 2] - nums[i])
            

        for i in range(n // 2 + 1, n):
            if nums[n // 2] > nums[i]:
                ans+=abs(nums[n // 2] - nums[i])

        return ans




s = Solution()
print(s.minOperationsToMakeMedianK([2,5,6,8,5], k = 4))