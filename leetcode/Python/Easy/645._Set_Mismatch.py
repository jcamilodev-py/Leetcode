from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = [0,0]
        for i in c:
            if c[i] == 2:
                ans[0] = i
        
        for i in range(1, len(nums)+1):
            if i not in c:
                ans[1] = i

        return ans


s = Solution()
print(s.findErrorNums([1,1]))        