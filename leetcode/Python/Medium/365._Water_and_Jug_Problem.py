from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        m = gcd(x, y)
        if target % m == 0 and target <= x + y:
            return True
        return False



s = Solution()
print(s.canMeasureWater(3,5,4))