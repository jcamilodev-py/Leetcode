from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dy1 = points[1][1] - points[0][1]
        dx1 = points[1][0] - points[0][0]
        dy2 = points[2][1] - points[1][1] 
        dx2 = points[2][0] - points[1][0]

        if dy1 * dx2 != dy2 * dx1:
            return True
        return False


s = Solution()
print(s.isBoomerang([[1,1],[2,2],[3,3]]))