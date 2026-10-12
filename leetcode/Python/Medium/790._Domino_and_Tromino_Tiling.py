class Solution:
    def numTilings(self, n: int) -> int:
        if n < 2:
            return 1
        mod = 10 ** 9 + 7

        dp = [1] * (n+1)
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] =  2 * dp[i-1] + dp[i-3]

        return dp[-1] % mod
        

s = Solution()
print(s.numTilings(3))