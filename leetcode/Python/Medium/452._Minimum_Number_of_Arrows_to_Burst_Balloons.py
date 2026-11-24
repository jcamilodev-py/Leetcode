class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        ans = len(points)

        prev = points[0][1]

        for i, j in points[1:]:
            if i > prev:
                prev = j
            else:
                ans-=1
                prev = min(prev, j)
        return ans


s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))