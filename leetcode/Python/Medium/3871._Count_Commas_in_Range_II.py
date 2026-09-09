class Solution:
    def countCommas(self, n: int) -> int:

        ans = 0
        d = 1

        while 10 ** (d - 1) <= n:
            l, h = 10 ** (d - 1), min(10 ** d-1, n)

            cg = h - l + 1

            c = (d-1) // 3
            ans+= cg * c
            d+=1

        return ans





s = Solution()
print(s.countCommas(1002))