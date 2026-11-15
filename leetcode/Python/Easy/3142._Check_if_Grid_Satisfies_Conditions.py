from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if j < m-1:
                    if grid[i][j] == grid[i][j+1]:
                        return False

                if i < n-1:
                    if grid[i][j] != grid[i+1][j]:
                        return False
        return True


s = Solution()
print(s.satisfiesConditions([[1,0,2],[1,0,2]]))