from math import sqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def repairs(time):
            count = 0
            for i in ranks:
                count+=int(sqrt(time / i))

            return count

        l,r = 1, ranks[0] * cars * cars

        ans = -1

        while l <= r:
            m = (l+r) // 2

            f = repairs(m)

            if f >= cars:
                ans = m
                r = m-1
            else:
                l = m+1

        return ans
        

s = Solution()
print(s.repairCars(ranks = [4,2,3,1], cars = 10))