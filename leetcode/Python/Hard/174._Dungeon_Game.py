class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])

        dp = [[0] * m for _ in range(n)]

        dp[n-1][m-1] = max(1, 1 - dungeon[n-1][m-1])

        for j in range(m-2, -1, -1):
            dp[n-1][j] = max(1, dp[n-1][j+1] - dungeon[n-1][j])

        for i in range(n-2, -1, -1):
            dp[i][m-1] = max(1, dp[i+1][m-1] - dungeon[i][m-1])


        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                v = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, v - dungeon[i][j])

        return dp[0][0]

        



s = Solution()
print(s.calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))