from collections import defaultdict
from typing import List
import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)

        for a, b, w in edges:
            adj[a].append((b,w))

        d = [[float('inf')] * (k+1) for _ in range(n)]
        d[0][1] = 0

        heap = [(0, 0, 1)]

        while heap:
            w, node, s = heapq.heappop(heap)

            if w > d[node][s]:
                continue

            if node == n-1:
                return w

            for nei, new_w in adj[node]:
                if labels[node] != labels[nei]:
                    new_s = 1
                else:
                    new_s = s+1

                if new_s > k:
                    continue

                if d[nei][new_s] > w + new_w:
                    d[nei][new_s] = w + new_w
                    heapq.heappush(heap, (w + new_w, nei, new_s))

        return -1




s = Solution()
print(s.shortestPath( n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1))