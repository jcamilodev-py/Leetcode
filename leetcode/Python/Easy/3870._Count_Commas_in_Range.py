class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return n - 999




s = Solution()
print(s.countCommas(2000))