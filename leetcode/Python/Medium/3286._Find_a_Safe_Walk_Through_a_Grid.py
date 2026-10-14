from typing import List
import heapq


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n,m = len(grid), len(grid[0])

        g = [[float('inf')] * m for _ in range(n)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
             
        g[0][0] = grid[0][0]
        h = [(g[0][0], 0, 0)]
        while h:
            cost, i, j = heapq.heappop(h)


            if cost == g[i][j]:
                for di, dj in dir:
                    ni, nj, = i + di, j + dj

                    if 0 <= ni < n and 0 <=nj < m:
                        v = cost + grid[ni][nj]
                        if v < g[ni][nj]:
                            g[ni][nj] = v
                            heapq.heappush(h, (v, ni, nj))
            if (i, j) == (n-1, m-1):
                return health - g[-1][-1] > 0

        return health - g[-1][-1] > 0
                



s = Solution()
print(s.findSafeWalk(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1))