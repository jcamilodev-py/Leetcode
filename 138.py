from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = float('inf')
        maximum = 0

        for i in nums:
            if i < minimum:
                minimum = i
            if i > maximum:
                 maximum = i
            
        while maximum != 0:
                minimum, maximum = maximum, minimum % maximum
        return minimum

s = Solution()
print(s.findGCD([7,5,6,8,3]))