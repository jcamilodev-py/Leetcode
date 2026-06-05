from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ans = 0
        rows, cols = len(grid), len(grid[0])

        def recursion(i,j):
            if i<0 or i >=rows or j < 0 or j >= cols:
                return 
            if grid[i][j] == "0":
                return
            elif (i,j) in seen:
                return
            
            seen.add((i,j))

            recursion(i+1,j)
            recursion(i-1,j)
            recursion(i,j+1)
            recursion(i,j-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    ans+=1
                    recursion(i,j)
        return ans


s = Solution()
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))