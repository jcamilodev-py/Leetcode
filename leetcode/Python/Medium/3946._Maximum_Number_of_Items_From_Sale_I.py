from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        gain = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    gain[i] += 1

        dp = [0] * (budget + 1)
        for i in range(n):
            p = items[i][1]
            for c in range(budget, p - 1, -1):
                dp[c] = max(dp[c], dp[c - p] + gain[i])

        minp = min(price for _, price in items)
        return max(dp[c] + (budget - c) // minp for c in range(budget + 1))


s = Solution()
print(s.maximumSaleItems([[6,2],[2,6],[3,4]], budget = 9))