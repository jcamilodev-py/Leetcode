from typing import List
import heapq
from collections import deque

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        r,c = len(grid), len(grid[0])

        arr = []

        for i in range(r):
            grid[i] = deque(sorted(grid[i], reverse=True))
            heapq.heappush(arr, (-grid[i][0], i))

        ans = 0

        c = [0] * r

        for _ in range(k):

            while True:
                v, i = heapq.heappop(arr)
                if c[i] < limits[i]:
                    c[i] +=1
                    ans+=v
                    grid[i].popleft()
                    if len(grid[i]) > 0:
                        heapq.heappush(arr, (-grid[i][0], i))
                    break
        return -ans
        

s = Solution()
print(s.maxSum(grid = [[1,2],[3,4]], limits = [1,2], k = 2))