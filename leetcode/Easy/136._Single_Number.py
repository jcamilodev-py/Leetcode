from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i



s = Solution()
print(s.singleNumber([4,1,2,1,2]))