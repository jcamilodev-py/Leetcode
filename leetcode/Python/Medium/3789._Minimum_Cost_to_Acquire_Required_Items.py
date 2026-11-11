class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        ab = abs(need1 - need2)

        r = cost1 if need1 > need2 else cost2

        return min(cost1 * need1 + cost2 * need2, costBoth * max(need1, need2), costBoth * m + r * ab)


s = Solution()
print(s.minimumCost(cost1 = 50, cost2 = 55, costBoth = 72, need1 = 5, need2 = 3))