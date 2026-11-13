from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        degree = [[0] * m for _ in range(n)]
        d = deque([])

        for i in range(n):
            for j in range(m):
                if matrix[max(i-1, 0)][j] > matrix[i][j]:
                    degree[i][j]+=1

                if matrix[min(i+1, n-1)][j] > matrix[i][j]:
                    degree[i][j]+=1

                if matrix[i][max(j-1, 0)] > matrix[i][j]:
                    degree[i][j]+=1

                if matrix[i][min(j+1, m-1)] > matrix[i][j]:
                    degree[i][j]+=1

                if degree[i][j] == 0:
                    d.append((i,j))

        ans = 0

        while d:
            ans+=1
            for _ in range(len(d)):
                i, j = d.popleft()
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] < matrix[i][j]:
                        degree[ni][nj]-=1

                        if degree[ni][nj] == 0:
                            d.append((ni, nj))

        return ans



        
s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))