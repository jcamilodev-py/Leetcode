class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):

            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if grid[i][j] == 1 or (i, j) in visited:
                return True

            visited.add((i, j))

            return dfs(i - 1, j) and dfs(i + 1, j) and dfs(i, j - 1) and dfs(i, j + 1)


        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        ans += 1

        return ans
                    




s = Solution()
print(s.closedIsland([
[0,0,1,1,0,1,0,0,1,0],
[1,1,0,1,1,0,1,1,1,0],
[1,0,1,1,1,0,0,1,1,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,0,0,1,1,1,0],
[0,1,0,1,0,1,0,1,1,1],
[1,0,1,0,1,1,0,0,0,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,0,0,1,0,1,0,1],
[1,1,1,0,1,1,0,1,1,0]]))