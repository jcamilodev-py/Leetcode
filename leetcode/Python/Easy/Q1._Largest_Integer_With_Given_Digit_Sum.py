class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0

        if s > 9 * n:
            return -1

        ans = []

        for i in range(n):
            d = min(9, s)
            ans.append(str(d))
            s-= d

        return int("".join(ans))



s = Solution()
print(s.largestInteger(3, 5))