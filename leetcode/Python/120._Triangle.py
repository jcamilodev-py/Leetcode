from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)

        for r in triangle[::-1]:
            for i, j in enumerate(r):
                dp[i] = j + min(dp[i], dp[i+1])

        return dp[0]




s = Solution()
print(s.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))