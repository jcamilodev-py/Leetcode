from typing import List
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if i == 0:
                ans+=1
            if (int(math.log10(i)) + 1) % 2 == 0:
                ans+=1
        return ans

        

s = Solution()
print(s.findNumbers([12,345,2,6,7896]))