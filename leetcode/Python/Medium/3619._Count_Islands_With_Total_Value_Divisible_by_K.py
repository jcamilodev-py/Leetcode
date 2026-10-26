from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        visit = set()
        ans = [0]

        def dfs(i,j, current_sum):
            if i < 0 or i == n or j < 0 or j == m:
                return
            if (i,j) in visit:
                return

            if grid[i][j] == 0:
                return

            visit.add((i,j))

            current_sum[0]+=grid[i][j]

            dfs(i+1,j, current_sum)
            dfs(i-1,j, current_sum)
            dfs(i,j+1, current_sum)
            dfs(i,j-1, current_sum)


        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and (i,j) not in visit:
                    total = [0]
                    dfs(i,j, total)
                    if total[0] % k == 0:
                        ans[0]+=1

        return ans[0]



            
            





s = Solution()
print(s.countIslands([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5))