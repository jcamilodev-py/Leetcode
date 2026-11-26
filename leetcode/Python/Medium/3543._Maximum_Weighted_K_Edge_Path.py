from functools import cache
from typing import List


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:

        adj = [[] for _ in range(n)]

        for u,v,w in edges:
            adj[u].append((v,w))

        @cache
        def dp(u, current_k, current_sum):
            if current_k == 0:
                return current_sum
            ans = -1

            for v, w in adj[u]:
                if current_sum + w < t:
                    ans = max(ans, dp(v, current_k - 1, current_sum + w))

            return ans
                    
        return max(dp(i,k,0) for i in range(n))

            





s = Solution()
print(s.maxWeight(n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4))