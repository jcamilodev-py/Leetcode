from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda idx: intervals[idx][0])
        sorted_intervals = [intervals[idx] for idx in order]
        starts = [iv[0] for iv in sorted_intervals]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] <= b[1] else b
        
        for i in range(n - 1, -1, -1):
            end_i = sorted_intervals[i][1]
            weight_i = sorted_intervals[i][2]
            j = bisect_right(starts, end_i)
            for k in range(4):
                no_tomar = dp[i + 1][k]
                score_j, idx_j = dp[j][k + 1]
                take_indices = tuple(sorted(idx_j + (order[i],)))
                tomar = (weight_i + score_j, take_indices)
                dp[i][k] = better(tomar, no_tomar)

        return list(dp[0][0][1])


s = Solution()
print(s.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]))