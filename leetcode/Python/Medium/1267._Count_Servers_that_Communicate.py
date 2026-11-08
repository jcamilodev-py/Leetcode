class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        r = [0] * n
        c = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r[i]+=1
                    c[j]+=1


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (r[i] > 1 or c[j] > 1):
                    ans+=1

        return ans




                





s = Solution()
print(s.countServers(grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))