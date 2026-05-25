from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = nums[0]


        for i in range(1, len(nums)):
            if i %2 != 0:
                ans-=nums[i]
            else:
                ans+=nums[i]
        return ans

s = Solution()
print(s.alternatingSum([]))