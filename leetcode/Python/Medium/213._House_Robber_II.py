from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        def rob2(nums):
            r1, r2 = 0,0
            for i in nums:
                temp = max(i + r1, r2)
                r1 = r2
                r2 = temp
            return r2

        return max(rob2(nums[1:]), rob2(nums[:n-1]))

s = Solution()
print(s.rob([2,3,2]))