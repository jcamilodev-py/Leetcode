from math import sqrt

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        
        return sqrt((max(x1, min(xCenter, x2)) - xCenter) ** 2 + (max(y1, min(yCenter, y2)) - yCenter)**2) <= radius



s = Solution()
print(s.checkOverlap(radius = 2, xCenter = 102, yCenter = 50, x1 = 0, y1 = 0, x2 = 100, y2 = 100))