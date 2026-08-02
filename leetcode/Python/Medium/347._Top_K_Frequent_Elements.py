from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []

        for i, j in c.items():
            if len(heap) < k:
                heapq.heappush(heap, (j, i))
            else:
                heapq.heappushpop(heap, (j, i))

        return [ans[1] for ans in heap]



s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], k = 2))