from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0

        c = Counter(nums)

        for i in c.values():
            ans+= int(i * (i-1) / 2)
        
        return ans



s = Solution()
print(s.numIdenticalPairs([1,1,1,1]))