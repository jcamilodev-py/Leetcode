from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        maximum = 0
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if (i,j) in seen:
                return 0
            
            seen.add((i,j))
            
            if grid[i][j] == 1:
                return 1 + dfs(i+1, j)+ dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in seen:
                    maximum = max(maximum, dfs(i, j))
        return maximum
        


s = Solution()
print(s.maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))