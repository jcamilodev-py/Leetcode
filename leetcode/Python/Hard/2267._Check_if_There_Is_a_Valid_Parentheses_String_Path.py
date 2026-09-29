class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        n, m = len(grid), len(grid[0])

        if grid[0][0] == ")" or grid[-1][-1] == "(" or (m + n - 1) % 2 != 0:
            return False

        dp = [[[False] * (m + n) for _ in range(m)] for _ in range(n)]

        dp[0][0][1] = True

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                h = 1 if grid[i][j] == "(" else -1

                for x in range(m + n):
                    t = i > 0 and dp[i-1][j][x]
                    d = j > 0 and dp[i][j-1][x]

                    if t or d:
                        new = x + h
                        if 0 <= new < m + n:
                            dp[i][j][new] = True

        return dp[n-1][m-1][0]



s = Solution()
print(s.hasValidPath(grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))