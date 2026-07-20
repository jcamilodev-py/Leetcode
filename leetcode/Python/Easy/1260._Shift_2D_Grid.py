from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        k%= (n * m)

        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                idx = i* m + j
                new_idx = (idx + k) % (n * m)
                nx, ny = new_idx // m, new_idx % m
                ans[nx][ny] = grid[i][j] 
        
        return ans



s = Solution()
print(s.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))