from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)
        seen = set(days)

        for i in range(1, days[-1]+1):
            if i in seen:
                dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]

        return dp[-1]





s = Solution()
print(s.mincostTickets([1,4,6,7,8,20], costs = [2,7,15]))