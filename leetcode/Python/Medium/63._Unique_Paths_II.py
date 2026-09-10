from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        for i in range(m):
            if obstacleGrid[0][i] == -1:
                break
            obstacleGrid[0][i] = 1

        for i in range(n):
            if obstacleGrid[i][0] == -1:
                break

            obstacleGrid[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == -1:
                    obstacleGrid[i][j] = 0

                elif obstacleGrid[i-1][j] == -1 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j]+= obstacleGrid[i][j-1]
                elif obstacleGrid[i-1][j] != -1 and obstacleGrid[i][j-1] == -1:
                    obstacleGrid[i][j]+= obstacleGrid[i-1][j]
                elif obstacleGrid[i-1][j] != -1 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[n-1][m-1] if obstacleGrid[n-1][m-1] != -1 else 0
                





s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))