from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]* (n+1)

        for i in range(1, n+1):
            dp[i] = float('inf')

            for s in [1,2,3]:
                j = i - s
                if j >= 0:
                    dp[i] = min(dp[i], dp[j] + costs[i-1] + (i - j)**2)
        
        return dp[n]
        



s = Solution()
print(s.climbStairs(n = 4, costs = [1,2,3,4]))