from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid[0])

        for i in grid:
            for j in range(m-1, -1, -1):
                if i[j] < 0:
                    ans+=1
                else:
                    break
        return ans





s = Solution()
print(s.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))