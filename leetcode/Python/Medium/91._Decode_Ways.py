class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            if s[0] != "0":
                return 1
            return 0
        
        dp = [1] * n

        dp[0] = 1 if s[0] != "0" else 0

        dp[1] = (dp[0] if s[1] != "0" else 0) + (1 if "10" <= s[0:2]<="26" else 0)

        for i in range(2, n):
            if s[i] != "0":
                if "10" <= s[i-1:i+1] <= "26":
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if "10" <= s[i-1:i+1] <= "26":
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0

        return dp[-1]

s = Solution()
print(s.numDecodings("227"))