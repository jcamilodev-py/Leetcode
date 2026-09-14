from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        seen = set()
        for i in mines:
            seen.add((i[0], i[1]))

        grid = [[0 if (i,j) in seen else 1 for j in range(n)] for i in range(n)]


        l = [[0] * n for _ in range(n)]
        r = [[0] * n for _ in range(n)]
        t = [[0] * n for _ in range(n)]
        d = [[0] * n for _ in range(n)]

        for i in range(n):
            current = 0
            for j in range(n):
                if grid[i][j] == 1:
                    current+=1
                else:
                    current = 0

                l[i][j] = current

        for i in range(n):
            current = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    current+=1
                else:
                    current = 0

                r[i][j] = current

        for j in range(n):
            current = 0
            for i in range(n):
                if grid[i][j] == 1:
                    current+=1
                else:
                    current = 0

                t[i][j] = current

        for j in range(n):
            current = 0
            for i in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    current+=1
                else:
                    current = 0

                d[i][j] = current

        ans = 0

        for i in range(n):
            for j in range(n):
                ans = max(ans, min(l[i][j], r[i][j], t[i][j], d[i][j]))

        
        return ans


                

s = Solution()
print(s.orderOfLargestPlusSign(n = 5, mines = [[4,2]]))