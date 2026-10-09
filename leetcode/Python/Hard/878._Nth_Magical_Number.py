from math import lcm

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ab = lcm(a, b)

        l, r = 1, n * min(a, b)

        while l < r:
            m = (l + r) // 2

            if ((m // a + m // b) - m // ab) >= n:
                r = m
            else:
                l = m+1

        return l % (10 ** 9 + 7)




s = Solution()
print(s.nthMagicalNumber(n = 4, a = 2, b = 3))