from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        zeros = 0
        for i, j in enumerate(nums):
            if j == 0:
                zeros+=1

            while zeros > 1:
                if nums[left] == 0:
                    zeros-=1
                left+=1

            ans = max(ans, i - left)

        return ans


s = Solution()
print(s.longestSubarray([1,1,1]))