from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

                    ans = max(ans, dp[i][j])

        return ans * ans 


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))