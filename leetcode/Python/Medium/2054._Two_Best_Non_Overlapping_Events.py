from typing import List
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        starts = [i[0] for i in events]

        dp = [[0] * 3 for _ in range(n+1)]


        for i in range(n-1, -1, -1):
            for k in range(2):
                j = bisect_right(starts, events[i][1])

                dp[i][k] = max(dp[i+1][k], events[i][2] + dp[j][k+1])

        return dp[0][0]


        



s = Solution()
print(s.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))