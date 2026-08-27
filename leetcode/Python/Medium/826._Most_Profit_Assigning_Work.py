from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        g = []
        n = len(difficulty)

        for i in range(n):
            g.append((difficulty[i], profit[i]))

        g.sort()
        ans = 0

        best = [0] * n
        best[0] = g[0][1]

        for i in range(1, n):
            best[i] = max(best[i-1], g[i][1])

        for i in worker:
            l, r = 0, n-1
            idx = -1

            while l <= r:
                m = (l + r) // 2

                if g[m][0] <= i:
                    idx = m
                    l = m + 1
                else:
                    r = m - 1

            if idx != -1:
                ans+=best[idx]

        return ans


            





s = Solution()
print(s.maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))