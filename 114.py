from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0

        for i,j in enumerate(nums):
            start = max(0, i - j)
            s = sum(nums[start: i+1])
            ans +=s
        return ans


s = Solution()
print(s.subarraySum([3,1,1,2]))