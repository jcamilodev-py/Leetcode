from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m = min(nums)
            for x,y in enumerate(nums):
                if y == m:
                    nums[x] = y*multiplier
                    break
                    
        return nums


s = Solution()
print(s.getFinalState([1,2], 3, 4))