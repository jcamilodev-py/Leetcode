class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0

        y = x / 2

        t = 1e-10
        m = 1000

        for _ in range(m):
            new_y = 0.5 * (y + x / y)
            if abs(new_y - y) < t:
                return int(new_y)

            y = new_y

        return int(y)


s = Solution()
print(s.mySqrt(8))