from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        n = len(grid)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1),(-1, -1), (1, -1)]

        visit = set({(0, 0)})


        d = deque([(0, 0, 1)])

        while d:
            vi, vj, ans = d.popleft()

            if (vi, vj) == (n-1, n-1):
                return ans

            for di, dj in dirs:
                ni, nj = vi + di, vj + dj

                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visit:
                    if grid[ni][nj] == 0:
                        visit.add((ni, nj))
                        d.append((ni, nj, ans+1))

        return -1
            





s = Solution()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))