from typing import List
from collections import Counter

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s = sorted(nums)
        if s[0] + s[1] <= s[2]:
            return "none"
        
        c = len(Counter(nums))
        
        if c == 1:
            return "equilateral"
        elif c == 2:
            return "isosceles"
        else:
            return "scalene"


        
s = Solution()
print(s.triangleType([5,3,8]))