class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])

        rows = [0] * n
        cols = [0] * m


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i]+=1
                    cols[j]+=1


        diff = [[None] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                diff[i][j] = rows[i] + cols[j] - (n - rows[i]) - (m - cols[j])

        return diff
                                                                  
                
s = Solution()
print(s.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))