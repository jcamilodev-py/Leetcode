from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        v = max(nums)
        ans = 0

        for i in nums:
            ans+= v - i

        return ans




s = Solution()
print(s.minMoves([4,4,5]))