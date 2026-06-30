from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        
        d = deque()
        fresh = 0
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    d.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        while d:
            size = len(d)
            for _ in range(size):
                i,j = d.popleft()
                if j+1 < cols and grid[i][j+1] == 1:
                    d.append((i, j+1))
                    grid[i][j+1] = 2
                    fresh-=1

                if  j-1 >= 0 and grid[i][j-1] == 1:
                    d.append((i, j-1))
                    grid[i][j-1] = 2
                    fresh-=1

                if  i+1 < rows and grid[i+1][j] == 1:
                    d.append((i+1, j))
                    grid[i+1][j] = 2
                    fresh-=1

                if  i-1 >= 0 and grid[i-1][j] == 1:
                    d.append((i-1, j))
                    grid[i-1][j] = 2
                    fresh-=1
            if len(d) > 0:
                minutes+=1

        return minutes if not fresh else -1
    

s = Solution()
print(s.orangesRotting([[2,1]]))