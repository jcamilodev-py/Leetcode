from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0

        def dfs(i):
            nonlocal ans

            if 2 * i > n:
                return cost[i-1]

            l = dfs(2*i)
            r = dfs(2*i + 1)

            ans+= abs(l - r)

            return cost[i-1] + max(l, r)

        dfs(1)
        return ans



s = Solution()
print(s.minIncrements(n = 15, cost = [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]))