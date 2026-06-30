from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n+1)
        for i in range(1, n+1):
            p[i] = p[i-1] + nums[i-1]
        
        for i in range(n):
            left = p[i] + nums[i]
            right = p[-1] - left

            if right == p[i]:
                return i
        return -1



s = Solution()
print(s.pivotIndex([2,1,-1]))