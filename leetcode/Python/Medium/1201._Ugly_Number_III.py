from math import lcm

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        ab = lcm(a,b)
        ac = lcm(a, c)
        bc = lcm(b,c)
        abc = lcm(ab, c)

        def f(x):
            return (x // a + x // b + x // c) - x // ab - x // ac - x // bc + x // abc

        l, r = 1, n * min(a, b, c)

        while l < r:
            m = (l + r) // 2

            if f(m) >= n:
                r = m
            else:
                l = m+1
        return l




s = Solution()
print(s.nthUglyNumber(n = 3, a = 2, b = 3, c = 5))