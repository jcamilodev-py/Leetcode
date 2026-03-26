from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product = product*i
    
        return  1 if product > 0 else -1 if product < 0 else 0

s = Solution()
print(s.arraySign([-1,-2,-3,-4,3,2,1]))