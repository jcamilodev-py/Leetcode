class Solution:
    def numSquares(self, n: int) -> int:
        arr = [1]

        for i in range(2, (int(n**0.5)+1)):
            arr.append(i*i)

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in arr:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j]+1)

        return dp[-1]
            




s = Solution()
print(s.numSquares(13))