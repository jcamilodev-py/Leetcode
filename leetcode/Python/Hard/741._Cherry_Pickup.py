class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)

        dp = [[grid[0][0]] * n for _ in range(n)]

        for i in range(1, n):
            if grid[0][i] == -1:
                dp[0][i] = float('-inf')
            else:
                dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, n):
            if grid[i][0] == -1:
                dp[i][0] = float('-inf')
            else:
                dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, n):
            for j in range(1, n):
                if grid[i][j] ==-1:
                    dp[i][j] = float('-inf')
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                    dp[i][j]+=grid[i][j]

        dp2 = [[[float('-inf')] * n for _ in range(n)] for _ in range(2 * n-1)]

        for k in range(2 * n - 1):
            for r1 in range(n):
                for r2 in range(n):
                    c1 = k - r1
                    c2 = k - r2

                    if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                        continue
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    if k == 0:
                        dp2[0][0][0] = grid[0][0]
                        continue

                    best = dp2[k-1][r1][r2]

                    if r1 > 0:
                        best = max(best, dp2[k - 1][r1 - 1][r2])
                    if r2 > 0:
                        best = max(best, dp2[k - 1][r1][r2 - 1])
                    if r1 > 0 and r2 > 0:
                        best = max(best, dp2[k - 1][r1 - 1][r2 - 1])

                    if best == float('-inf'):
                        continue

                    c = grid[r1][c1]
                    if r1 != r2:     
                        c += grid[r2][c2]

                    dp2[k][r1][r2] = best + c

        return max(0, dp2[2*n-2][n-1][n-1])

                    
s = Solution()
print(s.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))