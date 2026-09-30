from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        n, m = len(maze), len(maze[0])

        dist = [[-1] * m for _ in range(n)]

        d = deque([(entrance[0], entrance[1])])


        dist[entrance[0]][entrance[1]] = 0

        while d:

            f, c = d.popleft()

            for df, dc in [(-1,0), (1,0), (0,-1), (0,1)]:

                nf, nc = f + df, c + dc

                if 0 <= nf < n and 0 <= nc < m and maze[nf][nc] != "+" and dist[nf][nc] == -1:
                    dist[nf][nc] = dist[f][c] + 1

                    if nf == 0 or nc == 0 or nf == n-1 or nc == m-1:
                        return dist[nf][nc]

                    d.append((nf, nc))

        return -1

        
        



s = Solution()
print(s.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))