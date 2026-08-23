from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            v = True

            if i - k >= 0 and nums[i] <= nums[i - k]:
                v = False

            if i + k < n and nums[i] <= nums[i + k]:
                v = False

            if v:
                ans+=nums[i]

        return ans




s = Solution()
print(s.sumOfGoodNumbers([1,3,2,1,5,4], k = 2))