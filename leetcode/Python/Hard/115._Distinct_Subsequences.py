class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            ans = dp(i + 1, j)

            if s[i] == t[j]:
                ans+= dp(i+1, j+1)


            return ans

        return dp(0, 0)




s = Solution()
print(s.numDistinct("rabbbit", t = "rabbit"))