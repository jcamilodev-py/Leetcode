from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if j + 1 == len(grid[i]):
                        ans+=1
                    elif grid[i][j + 1] == 0:
                        ans+=1

                    if j - 1 < 0:
                        ans+=1
                    elif grid[i][j - 1] == 0:
                        ans+=1

                    if i - 1 < 0:
                        ans+=1
                    elif grid[i - 1][j] == 0:
                        ans+=1

                    if i + 1 == n:
                        ans+=1
                    elif grid[i + 1][j] == 0:
                        ans+=1

        return ans
                    

                

s = Solution()
print(s.islandPerimeter([[0,1]]))