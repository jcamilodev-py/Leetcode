class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        seen = set()
        i, j = 0, 0

        while 0 <= i < n and 0 <= j < m and (i,j) not in seen:
            seen.add((i,j))

            if grid[i][j] == "R":
                if (i,j+1) in seen or j+1 == m:
                    return [i,j]
                j+=1
            elif grid[i][j] == "L":
                if (i,j-1) in seen or j-1 < 0:
                    return [i,j]
                j-=1
            elif grid[i][j] == "D":
                if (i+1,j) in seen or i+1 == n:
                    return [i,j]
                i+=1
            else:
                if (i-1,j) in seen or i-1 < 0:
                    return [i,j]
                i-=1

        return [i,j]

        



s = Solution()
print(s.lastVisitedCell([["R","R","R"]]))