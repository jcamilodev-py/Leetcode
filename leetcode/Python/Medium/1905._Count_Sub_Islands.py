class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        ans = 0

        visited = set()

        def dfs(i, j, value):
            if i < 0 or j < 0 or i == n or j == m:
                return
            if grid2[i][j] == 0:
                return

            if (i,j) in visited:
                return

            visited.add((i,j))

            if grid1[i][j] == 0:
                value[0] = False


            dfs(i+1, j, value)
            dfs(i-1, j, value)
            dfs(i, j+1, value)
            dfs(i, j-1, value)

            return value[0]

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    if dfs(i,j, [True]):
                        ans+=1
        return ans
            





s = Solution()
print(s.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))