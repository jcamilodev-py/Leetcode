from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        e = defaultdict(list)

        for u, v, w in times:
            e[u].append((v, w))

        min_heap = [(0, k)]

        v = set()

        ans = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in v:
                continue
            v.add(n1)

            ans = max(ans, w1)

            for n2, w2 in e[n1]:
                if n2 not in v:
                    heapq.heappush(min_heap,(w1 + w2, n2))


        return ans if len(v) == n else -1
        




s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))