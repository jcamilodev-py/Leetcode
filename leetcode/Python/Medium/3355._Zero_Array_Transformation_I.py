from typing import List
from collections import Counter
from collections.abc import Iterable


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)
        diff = [0] * (n+1)

        for i,j in queries:
            diff[i]+=1
            diff[j+1]-=1

        p = [0] * n

        p[0] = diff[0]

        for i in range(1, n):
            p[i] = p[i-1] + diff[i]

        for i in range(n):
            if nums[i] > p[i]:
                return False
        return True
        



s = Solution()
print(s.isZeroArray([1,0,1], queries = [[0,2]]))