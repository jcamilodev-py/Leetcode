from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])

        dist = [[0 if mat[i][j] == 0 else -1 for j in range(m)] for i in range(n)]

        d = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    d.append((i,j))

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while d:
            i, j = d.popleft()

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    d.append((ni, nj))

        return dist
                
        


s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))