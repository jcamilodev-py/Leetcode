# from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        adj = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[4,2]}

        # @cache
        # def dp(i, lenn):
        #     if lenn == n:
        #         return 1

        #     ans = 0
            
        #     for j in adj[i]:
        #         ans+=dp(j, lenn+1)

        #     return ans % mod


        # return sum(dp(i, 1) for i in range(10)) % mod

        dp = [1] * 10

        for _ in range(n-1):
            nxt = [0] * 10

            for v in range(10):
                for u in adj[v]:
                    nxt[v] = (nxt[v] + dp[u]) % mod
            dp = nxt

        return sum(dp) % mod


s = Solution()
print(s.knightDialer(20))