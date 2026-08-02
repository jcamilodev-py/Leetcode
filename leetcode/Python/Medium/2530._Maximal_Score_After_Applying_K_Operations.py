from typing import List
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for i in range(k):
            ans+=-nums[0]
            v = ceil(-nums[0] / 3)
            heapq.heappushpop(nums, -v)

        return ans



s = Solution()
print(s.maxKelements([1,10,3,3,3], k = 3))