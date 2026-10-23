class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1)], dp[i-1][j], dp[i-1][min(n-1, j+1)])

        return min(dp[n-1])



s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))